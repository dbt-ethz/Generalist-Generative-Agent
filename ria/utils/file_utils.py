import ast
import json
import os
import re
from pathlib import Path


def _resolve_path(*parts) -> Path:
    if len(parts) == 1 and isinstance(parts[0], (list, tuple)):
        parts = tuple(parts[0])
    path = os.path.join(*(os.fspath(part) for part in parts))
    path = os.path.expandvars(os.path.expanduser(path))
    return Path(path)


def load_text(*path_parts, by_lines=False):
    path = _resolve_path(*path_parts)
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        if by_lines:
            return handle.readlines()
        return handle.read()


def json_load(*path_parts, **kwargs):
    path = _resolve_path(*path_parts)
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle, **kwargs)


def json_dump(data, *path_parts, **kwargs):
    path = _resolve_path(*path_parts)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, **kwargs)


def load_metaphors_data(folder):
    folder_path = _resolve_path(folder)
    if not folder_path.is_dir():
        return {}

    metaphor_files = {}
    for file_path in sorted(folder_path.glob("*.json")):
        data = json_load(file_path)
        if isinstance(data, dict):
            data = {key: value for key, value in data.items() if key != "timestamp"}
        metaphor_files[file_path.name] = data
    return metaphor_files


def load_skill_libs(folder):
    skills_dir = _resolve_path(folder)
    if not skills_dir.is_dir():
        return {}

    skill_libs = {}
    for interpretation_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        examples = {}
        for design_dir in sorted(path for path in interpretation_dir.iterdir() if path.is_dir()):
            function_code = None
            code_summary = None

            for file_path in sorted(design_dir.iterdir()):
                if file_path.suffix == ".py":
                    function_code = extract_variable_from_file(file_path, "function_code")
                elif file_path.suffix == ".md":
                    code_summary = load_text(file_path)

            if function_code and code_summary:
                example_id = len(examples) + 1
                examples[f"example_{example_id}"] = {
                    "function_code": function_code,
                    "code_summary": code_summary,
                }

        if examples:
            skill_libs[f"{interpretation_dir.name}.json"] = examples

    return skill_libs


def extract_variable_from_file(file_path, var_name):
    content = load_text(file_path)

    triple_quote_patterns = [
        rf"{var_name}\s*=\s*\"\"\"(.*?)\"\"\"",
        rf"{var_name}\s*=\s*'''(.*?)'''",
    ]
    for pattern in triple_quote_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1)

    try:
        tree = ast.parse(content)
    except SyntaxError:
        return None

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == var_name:
                if isinstance(node.value, ast.Str):
                    return node.value.s
                if isinstance(node.value, ast.Constant) and isinstance(
                    node.value.value, (str, int, float)
                ):
                    return node.value.value

    return None
