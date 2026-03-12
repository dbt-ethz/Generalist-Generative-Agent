import argparse
import os
from datetime import datetime

from rich import print as rprint

from ria.agents import InterpretationAgent
from ria.utils import json_dump, json_load, to_snake_case

DEFAULT_INTERPRETATIONS_DIR = os.path.join(
    os.path.dirname(__file__), "output/experiment_data/02_interpretations"
)
DEFAULT_METAPHORS_DIR = os.path.join(
    os.path.dirname(__file__), "output/experiment_data/01_metaphors_expanded"
)

N_INTERPRETATIONS = 5  # Global variable for the number of interpretations to generate


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path

def list_previous_metaphors(folder):
    previously_generated_metaphors = []
    for file in os.listdir(folder):
        if file.endswith(".json"):
            data = json_load(os.path.join(folder, file))
            idea_str = data["metaphor"]
            previously_generated_metaphors.append(idea_str)
    list_str = "\n".join(previously_generated_metaphors)
    if list_str:
        list_str = f"Previously generated metaphors:\n{list_str}"
    return list_str

def load_metaphors_data(folder):
    all_metaphors_dict = {}
    for file in sorted(os.listdir(folder)):
        if file.endswith(".json"):
            data = json_load(f"{folder}/{file}")
            if "timestamp" in data:
                del data["timestamp"]  # Remove the 'timestamp' key if it exists
            all_metaphors_dict[file] = data
    return all_metaphors_dict

def get_next_interpretation_id(number_part, interpretations_dir):
    interpretation_files = [
        f for f in os.listdir(interpretations_dir)
        if f.startswith(f"{number_part}_")
    ]
    interpretation_ids = [int(f.split("_")[1]) for f in interpretation_files]
    return max(interpretation_ids) + 1 if interpretation_ids else 1

def save_interpretation(
    interpretation,
    metaphor_data,
    number_part,
    interpretation_id,
    interpretations_dir,
):
    filename = to_snake_case(metaphor_data["metaphor"])
    data = interpretation.dict()
    data["metaphor"] = metaphor_data["metaphor"]
    data["key_traits"] = metaphor_data["key_traits"]
    timestr = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    data["timestamp"] = timestr
    padded_id = str(interpretation_id).zfill(4)
    json_dump(
        data, f"{interpretations_dir}/{number_part}_{padded_id}_{filename}.json"
    )

def run_interpretation_for_all_metaphors(
    metaphors_dir=DEFAULT_METAPHORS_DIR,
    interpretations_dir=DEFAULT_INTERPRETATIONS_DIR,
    metaphor_ids_to_interpret=None,
    versions=N_INTERPRETATIONS,
):
    interpretations_dir = ensure_dir(interpretations_dir)
    interpretation_agent = InterpretationAgent()
    metaphors = load_metaphors_data(metaphors_dir)

    for metaphor_file, metaphor_data in metaphors.items():
        number_part = metaphor_file.split("_")[0]
        metaphor_id = int(number_part)
        if metaphor_ids_to_interpret and metaphor_id not in metaphor_ids_to_interpret:
            continue
        interpretation_id = get_next_interpretation_id(number_part, interpretations_dir)

        history = {}
        for i in range(versions):
            interpretation = interpretation_agent.suggest_design_task(metaphor_data, history)
            history[f'example_{i+1}'] = interpretation.dict()
            rprint(interpretation)
            save_interpretation(
                interpretation,
                metaphor_data,
                number_part,
                interpretation_id + i,
                interpretations_dir,
            )

def run_interpretation_for_single_metaphor(
    filename,
    metaphors_dir=DEFAULT_METAPHORS_DIR,
    interpretations_dir=DEFAULT_INTERPRETATIONS_DIR,
    versions=N_INTERPRETATIONS,
):
    interpretations_dir = ensure_dir(interpretations_dir)
    filepath = os.path.join(metaphors_dir, filename)
    if not os.path.exists(filepath):
        rprint(f"File {filename} does not exist in the specified folder.")
        return


    interpretation_agent = InterpretationAgent()
    metaphor_data = json_load(filepath)
    if "timestamp" in metaphor_data:
        del metaphor_data["timestamp"]  # Remove the 'timestamp' key if it exists

    number_part = filename.split("_")[0]
    interpretation_id = get_next_interpretation_id(number_part, interpretations_dir)

    history = {}
    for i in range(versions):        
        interpretation = interpretation_agent.suggest_design_task(metaphor_data, history)
        history[f'example_{i+1}'] = interpretation.dict()
        rprint(interpretation)
        save_interpretation(
            interpretation,
            metaphor_data,
            number_part,
            interpretation_id + i,
            interpretations_dir,
        )


def parse_args():
    parser = argparse.ArgumentParser(description="Run the interpretation agent.")
    parser.add_argument(
        "--metaphors-dir",
        default=DEFAULT_METAPHORS_DIR,
        help="Directory containing metaphor JSON files.",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_INTERPRETATIONS_DIR,
        help="Directory where interpretation JSON files will be written.",
    )
    parser.add_argument(
        "--versions",
        type=int,
        default=N_INTERPRETATIONS,
        help="Number of interpretations to generate per metaphor.",
    )
    parser.add_argument(
        "--metaphor-ids",
        nargs="+",
        type=int,
        default=None,
        help="Subset of metaphor IDs to process.",
    )
    parser.add_argument(
        "--filename",
        default=None,
        help="Specific metaphor filename to process.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.filename:
        run_interpretation_for_single_metaphor(
            args.filename,
            metaphors_dir=args.metaphors_dir,
            interpretations_dir=args.output_dir,
            versions=args.versions,
        )
    else:
        run_interpretation_for_all_metaphors(
            metaphors_dir=args.metaphors_dir,
            interpretations_dir=args.output_dir,
            metaphor_ids_to_interpret=args.metaphor_ids,
            versions=args.versions,
        )
