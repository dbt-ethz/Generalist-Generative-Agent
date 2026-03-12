import ast
import json
import os
import re
import shutil
import socket
from typing import List

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)
from langchain_openai import ChatOpenAI

from ria.prompts import load_prompt

load_dotenv()

MODEL_NAME_DEFAULT = "gpt-4o"


def clean_code_string(code_string):
    cleaned = re.sub(r"```[a-zA-Z]*\n|```", "", code_string).strip()
    lines = cleaned.splitlines()

    for index, line in enumerate(lines):
        if line.startswith("def "):
            lines = lines[index:]
            break

    while lines:
        candidate = "\n".join(lines).strip()
        try:
            tree = ast.parse(candidate)
        except SyntaxError:
            lines.pop()
            continue
        if any(isinstance(node, ast.FunctionDef) for node in tree.body):
            return candidate
        break

    return cleaned


def concat_calls_code(example_calls: List[str]):
    lines = [
        "import ghpythonlib.treehelpers as th",
        "geometry_states = []",
    ]
    for index, call in enumerate(example_calls, start=1):
        lines.extend(
            [
                f"# Generate sample geometry {index}/{len(example_calls)}",
                call,
                "geometry = list(geometry) if not isinstance(geometry, list) else geometry",
                "geometry_states.append(geometry)",
                "",
            ]
        )
    lines.extend(
        [
            "# Convert the list of geometries to a Grasshopper DataTree",
            "geometry_states = th.list_to_tree(geometry_states)",
        ]
    )
    return "".join(f"    {line}\n" if line else "\n" for line in lines)


def _prepare_code_for_gh(function_code: str, example_calls: List[str]):
    calls_code = concat_calls_code(example_calls)
    escaped_function_code = function_code.replace('"""', '\\"""')
    return (
        "#! python 3\n"
        f'function_code = """{escaped_function_code}"""\n\n'
        "try:\n"
        "    exec(function_code)\n"
        f"{calls_code}"
        '    print("success")\n'
        "except Exception as e:\n"
        '    print("Error: ", e)\n'
    )


def _send_code_to_grasshopper(message):
    server_address = ("localhost", 12346)
    receive_server_address = ("localhost", 12347)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as send_socket:
        send_socket.sendto(message.encode(), server_address)
        print(f"Sent: {message}")

    print("Message sent. Waiting for response...")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as receive_socket:
        receive_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        receive_socket.bind(receive_server_address)
        data, addr = receive_socket.recvfrom(4096)
        print(f"Received response from {addr}.")
        print("Closed socket")
        return data.decode()


def save_script_to_file(path, gh_code, interpretation_filename, summary):
    func_name = gh_code.split("def ")[1].split("(")[0]
    script_path = os.path.join(path, f"{func_name}.py")
    summary_string = f'""" Summary:\n{summary}"""\n\n'
    with open(script_path, "w", encoding="utf-8") as handle:
        handle.write(f"# Created for {interpretation_filename}\n\n")
        handle.write(summary_string)
        handle.write(gh_code)
    print(f"Python script saved as {script_path}")


def get_design_folder_name(output_dir, interpretation_filename):
    interpretation_name = interpretation_filename.split(".")[0]
    interpretation_dir = os.path.join(output_dir, interpretation_name)

    existing_folders = (
        [
            name
            for name in os.listdir(interpretation_dir)
            if os.path.isdir(os.path.join(interpretation_dir, name))
        ]
        if os.path.exists(interpretation_dir)
        else []
    )
    existing_ids = [
        int(folder.split("_")[2])
        for folder in existing_folders
        if len(folder.split("_")) > 2 and folder.split("_")[2].isdigit()
    ]
    next_id = max(existing_ids, default=0) + 1

    dir_name = os.path.basename(interpretation_dir).split("_")
    dir_name.insert(2, f"{next_id:04n}")
    return os.path.join(interpretation_dir, "_".join(dir_name))


class GHCodeAgent:
    def __init__(
        self,
        model_name=MODEL_NAME_DEFAULT,
        use_framework="RhinoCommon",
        do_not_use_framework="rhinoscriptsyntax",
    ):
        model = ChatOpenAI(model=model_name, timeout=60)
        mini_model = ChatOpenAI(model="gpt-4o-mini", timeout=10)

        system_prompt = PromptTemplate(
            template=load_prompt("gh_code", ext="md"),
            input_variables=[],
            partial_variables={
                "use_framework": use_framework,
                "do_not_use_framework": do_not_use_framework,
            },
        )
        prompt_template = ChatPromptTemplate.from_messages(
            [
                HumanMessagePromptTemplate(prompt=system_prompt),
                (
                    "user",
                    "Create a function for Grasshopper Python that can create an "
                    "architectural Concept Model adhering to the provided metaphor "
                    "and design task below. The function must take relevant "
                    "parameters as input to parametrically create the geometry of "
                    "the Concept Model, along with any needed helper geometry "
                    "objects. The function returns a list of 3D geometries only "
                    "(breps, surfaces, or meshes). Include a docstring that "
                    "describes the function's purpose, inputs, and outputs. Any "
                    "needed imports must be done in the function body. Return ONLY "
                    "THE CODE OF THE FUNCTION:\n\n{metaphor}.\n\n{skill_libs}",
                ),
            ]
        )
        error_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "user",
                    "Please fix the error in the function below in response to the "
                    "error message. Return ONLY THE CODE OF THE FIXED FUNCTION:\n\n"
                    "{code}\n\nError Message:\n{error}",
                ),
            ]
        )
        summary_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "user",
                    "Briefly explain in 100 words how the function below generates "
                    "an architectural concept model in response to the metaphor "
                    "and design task provided.\n\nMetaphor:\n{metaphor}\n\nCode:\n"
                    "{code}",
                ),
            ]
        )
        usage_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "user",
                    "Suggest ONE example usage for the function below given as "
                    "'geometry = function_name(parameter1, parameter2, etc.)'. "
                    "Return ONLY THE CODE.\n\nFunction Code:\n\n{code}\n\n"
                    "{previously_generated}",
                ),
            ]
        )

        self.skill_history_prompt = (
            "Below are previously generated functions for the same metaphor and "
            "design task. Try to apply a different approach this time while "
            "adhering to the provided metaphor and design task.\n\nPreviously "
            "generated functions:\n\n"
        )
        self.chain = prompt_template | model | StrOutputParser()
        self.error_chain = error_prompt_template | model | StrOutputParser()
        self.summary_chain = summary_prompt_template | mini_model | StrOutputParser()
        self.usage_chain = usage_prompt_template | mini_model | StrOutputParser()

    def _suggest_example_usage(self, code: str, previous_example_usages=None):
        if previous_example_usages:
            previously_generated = "Do not repeat the following example usages:\n\n"
            previously_generated += "\n".join(previous_example_usages)
        else:
            previously_generated = ""

        return self.usage_chain.invoke(
            {
                "code": code,
                "previously_generated": previously_generated,
            }
        )

    def generate_code(
        self,
        interpretation_data,
        interpretation_filename,
        skill_libs,
        output_dir,
        number_of_attempts=5,
        number_of_example_usages=3,
    ):
        error_message = None
        generated_gh_code = None
        progress_log = []
        design_output_dir = get_design_folder_name(output_dir, interpretation_filename)
        skill_history_text = (
            f"{self.skill_history_prompt}{skill_libs}" if skill_libs else ""
        )

        for attempt in range(number_of_attempts):
            if attempt == 0:
                print("Invoking chain for initial code generation.")
            else:
                print(
                    f"Retrying GH code generation (Attempt {attempt + 1}/{number_of_attempts})."
                )

            if error_message and generated_gh_code:
                generated_gh_code = self.error_chain.invoke(
                    {"code": generated_gh_code, "error": error_message}
                )
            else:
                generated_gh_code = self.chain.invoke(
                    {
                        "metaphor": interpretation_data,
                        "skill_libs": skill_history_text,
                    }
                )

            generated_gh_code = clean_code_string(generated_gh_code)
            print(f"Generated GH code:\n{generated_gh_code}")

            example_usages = []
            for _ in range(number_of_example_usages):
                example_usage = self._suggest_example_usage(
                    generated_gh_code,
                    previous_example_usages=example_usages,
                )
                example_usage = clean_code_string(example_usage)
                print(f"Example usage: {example_usage}")
                example_usages.append(example_usage)

            code_for_gh = _prepare_code_for_gh(generated_gh_code, example_usages)
            response = _send_code_to_grasshopper(code_for_gh)
            print(
                f"Response from GH (Attempt {attempt + 1}):\n=====\n{response}\n=====\n"
            )

            data = json.loads(response)
            script_log = data["script_log"]

            os.makedirs(design_output_dir, exist_ok=True)
            progress_log.append(
                {"attempt": attempt, "log": script_log, "code": code_for_gh}
            )
            with open(
                os.path.join(design_output_dir, "progress_log.json"),
                "w",
                encoding="utf-8",
            ) as handle:
                json.dump(progress_log, handle, indent=2)

            if script_log.strip().endswith("success"):
                print("Success! Code executed successfully.")

                obj_file_paths = data["obj_file_paths"]
                if obj_file_paths is None:
                    print("No OBJ files were created.")
                    return generated_gh_code, False

                for index, obj_file_path in enumerate(obj_file_paths):
                    obj_file_output_path = os.path.join(
                        design_output_dir, f"{index:02}_3d_model.obj"
                    )
                    print(obj_file_path)
                    shutil.copy2(obj_file_path, obj_file_output_path)
                    print(
                        f"Obj file {index}/{len(obj_file_paths)} saved as {obj_file_output_path}"
                    )

                code_summary = self.summary_chain.invoke(
                    {
                        "metaphor": interpretation_data,
                        "code": code_for_gh,
                    }
                )
                save_script_to_file(
                    design_output_dir,
                    code_for_gh,
                    interpretation_filename,
                    code_summary,
                )
                with open(
                    os.path.join(design_output_dir, "code_summary.md"),
                    "w",
                    encoding="utf-8",
                ) as handle:
                    handle.write(code_summary)
                with open(
                    os.path.join(design_output_dir, interpretation_filename),
                    "w",
                    encoding="utf-8",
                ) as handle:
                    json.dump(interpretation_data, handle)

                print("Success! GH code generated and saved.")
                return generated_gh_code, True

            error_message = script_log

        print("All attempts failed.")
        return generated_gh_code, False
