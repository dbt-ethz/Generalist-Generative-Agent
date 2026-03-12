import argparse
import copy
import os

from rich import print as rprint

from ria.agents import GHCodeAgent
from ria.utils import load_metaphors_data, load_skill_libs

ROOT_DIR = os.path.dirname(__file__)
DEFAULT_INTERPRETATIONS_DIR = os.path.join(
    ROOT_DIR, "output", "experiment_data", "02_interpretations"
)
DEFAULT_HISTORY_SKILLS_DIR = os.path.join(
    ROOT_DIR, "output", "experiment_data", "03_designs_H_gpt-4o"
)
DEFAULT_MODE = "history"
DEFAULT_MODEL = "gpt-4o"
DEFAULT_DESIGNS_PER_INTERPRETATION = 5
DEFAULT_ATTEMPTS = 5
DEFAULT_EXAMPLE_USAGES = 5
USE_FRAMEWORK = "RhinoCommon"
DO_NOT_USE_FRAMEWORK = "rhinoscriptsyntax"

MODE_CONFIGS = {
    "metaphor": {
        "history": False,
        "keys_to_keep": ["metaphor"],
        "default_output_dir": os.path.join(
            ROOT_DIR, "output", "experiment_data", "03_designs_gpt-4o_metaphor"
        ),
    },
    "design-task": {
        "history": False,
        "keys_to_keep": [
            "metaphor",
            "key_traits",
            "implications_form",
            "design_task",
        ],
        "default_output_dir": os.path.join(
            ROOT_DIR, "output", "experiment_data", "03_designs_gpt-4o_design_task"
        ),
    },
    "history": {
        "history": True,
        "keys_to_keep": [
            "metaphor",
            "key_traits",
            "implications_form",
            "design_task",
        ],
        "default_output_dir": os.path.join(
            ROOT_DIR, "output", "experiment_data", "03_designs_H_gpt-4o"
        ),
    },
}


def prepare_prompt_data(interpretation_data, keys_to_keep):
    return {
        key: interpretation_data[key]
        for key in keys_to_keep
        if key in interpretation_data
    }


def select_interpretations(all_interpretations, filename=None, interpretation_ids=None):
    if filename:
        if filename not in all_interpretations:
            raise FileNotFoundError(f"Interpretation file not found: {filename}")
        return {filename: all_interpretations[filename]}

    if not interpretation_ids:
        return all_interpretations

    selected = {}
    interpretation_ids = set(interpretation_ids)
    for interpretation_filename, interpretation_data in all_interpretations.items():
        interpretation_id = int(interpretation_filename.split("_")[0])
        if interpretation_id in interpretation_ids:
            selected[interpretation_filename] = interpretation_data

    return selected


def prepare_skill_history(skill_libs, interpretation_filename, history_on, evaluation_on):
    if not (history_on or evaluation_on):
        return None

    previous_generated_gh_skills = skill_libs.get(interpretation_filename)
    if not previous_generated_gh_skills:
        return None

    previous_generated_gh_skills = copy.deepcopy(previous_generated_gh_skills)
    if history_on and not evaluation_on:
        for example_data in previous_generated_gh_skills.values():
            example_data.pop("evaluation", None)

    return previous_generated_gh_skills


def parse_args():
    parser = argparse.ArgumentParser(description="Run the GH code agent.")
    parser.add_argument(
        "--mode",
        choices=sorted(MODE_CONFIGS),
        default=DEFAULT_MODE,
        help=(
            "Generation mode: 'metaphor' uses only the metaphor text, "
            "'design-task' uses the full interpretation, and 'history' also "
            "adds prior GH runs as few-shot history."
        ),
    )
    parser.add_argument(
        "--interpretations-dir",
        default=DEFAULT_INTERPRETATIONS_DIR,
        help="Directory containing interpretation JSON files.",
    )
    parser.add_argument(
        "--skills-dir",
        default=None,
        help="Directory containing prior GH runs used as few-shot skills.",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Directory where generated GH runs will be written.",
    )
    parser.add_argument(
        "--filename",
        default=None,
        help="Specific interpretation filename to process.",
    )
    parser.add_argument(
        "--interpretation-ids",
        nargs="+",
        type=int,
        default=None,
        help="Subset of interpretation IDs to process.",
    )
    parser.add_argument(
        "--designs-per-interpretation",
        type=int,
        default=DEFAULT_DESIGNS_PER_INTERPRETATION,
        help="How many GH design runs to create per interpretation.",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=DEFAULT_ATTEMPTS,
        help="Maximum retries per GH design run.",
    )
    parser.add_argument(
        "--example-usages",
        type=int,
        default=DEFAULT_EXAMPLE_USAGES,
        help="How many parameter variations to ask for in each GH design run.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="OpenAI model to use for GH code generation.",
    )
    parser.add_argument(
        "--history",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="Override whether to use prior runs as few-shot history.",
    )
    parser.add_argument(
        "--evaluation",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Include evaluation metadata in the few-shot history when present.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    mode_config = MODE_CONFIGS[args.mode]
    history_on = mode_config["history"] if args.history is None else args.history
    skills_dir = args.skills_dir or DEFAULT_HISTORY_SKILLS_DIR
    output_dir = args.output_dir or mode_config["default_output_dir"]

    rprint(
        {
            "mode": args.mode,
            "history": history_on,
            "interpretation_keys": mode_config["keys_to_keep"],
            "skills_dir": skills_dir if (history_on or args.evaluation) else None,
            "output_dir": output_dir,
        }
    )

    gh_code_agent = GHCodeAgent(
        model_name=args.model,
        use_framework=USE_FRAMEWORK,
        do_not_use_framework=DO_NOT_USE_FRAMEWORK,
    )

    full_interpretations = load_metaphors_data(args.interpretations_dir)
    interpretations_to_model = select_interpretations(
        full_interpretations,
        filename=args.filename,
        interpretation_ids=args.interpretation_ids,
    )
    if not interpretations_to_model:
        raise ValueError("No interpretation files matched the provided selection.")

    skill_libs = {}
    if history_on or args.evaluation:
        if not os.path.isdir(skills_dir):
            raise FileNotFoundError(f"Skills directory not found: {skills_dir}")
        skill_libs = load_skill_libs(skills_dir)

    total_count_generations = (
        len(interpretations_to_model) * args.designs_per_interpretation
    )
    counter = 0

    for interpretation_filename, interpretation_data in interpretations_to_model.items():
        print("Will create geometry for this interpretation:")
        prompt_data = prepare_prompt_data(
            interpretation_data,
            mode_config["keys_to_keep"],
        )
        rprint(prompt_data)

        previous_generated_gh_skills = prepare_skill_history(
            skill_libs,
            interpretation_filename,
            history_on=history_on,
            evaluation_on=args.evaluation,
        )
        if previous_generated_gh_skills:
            print(
                f"Using {len(previous_generated_gh_skills)} prior runs as few-shot skill history."
            )
        else:
            print("No prior GH skill history found for this interpretation.")

        for i in range(args.designs_per_interpretation):
            counter += 1
            print(
                f"Generating GH skill for {interpretation_filename} "
                f"({i + 1}/{args.designs_per_interpretation})"
            )
            _, success = gh_code_agent.generate_code(
                prompt_data,
                interpretation_filename,
                skill_libs=previous_generated_gh_skills,
                output_dir=output_dir,
                number_of_attempts=args.attempts,
                number_of_example_usages=args.example_usages,
            )

            if not success:
                print("Failed to generate GH skill.")
            else:
                print(f"Generated GH skill - progress: {counter}/{total_count_generations}")

    print("Done.")


if __name__ == "__main__":
    main()
