import argparse
import os
from datetime import datetime

from rich import print as rprint

from ria.agents import MetaphorAgent
from ria.utils import json_dump, json_load, to_snake_case

DEFAULT_METAPHORS_DIR = os.path.join(
    os.path.dirname(__file__), "output/experiment_data/01_metaphors_expanded"
)
DEFAULT_METAPHORS_LIST_FILE = os.path.join(
    os.path.dirname(__file__),
    "output/experiment_data/00_metaphors_list/metaphors_to_expand.txt",
)


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)
    return path


def load_metaphors_to_expand(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return [
            line.strip()
            for line in handle.readlines()
            if line.strip() and not line.lstrip().startswith("#")
        ]


def load_metaphors_data(folder):
    all_metaphors_dict = {}
    for file in sorted(os.listdir(folder)):
        if file.endswith(".json"):
            data = json_load(f"{folder}/{file}")
            if "timestamp" in data:
                del data["timestamp"]  # Remove the 'timestamp' key if it exists
            all_metaphors_dict[file] = data
    return all_metaphors_dict


def get_metaphor_count(metaphors_dict):
    numbers = []
    for filename in metaphors_dict.keys():
        number_part = filename.split("_")[0]
        try:
            numbers.append(int(number_part))
        except ValueError:
            pass
    return max(numbers) if numbers else 0


def list_previous_metaphors(metaphors_dict, cutoff=None):
    previously_generated_metaphors = [
        data["metaphor"]
        for counter, (file, data) in enumerate(metaphors_dict.items())
        if not cutoff or counter >= cutoff
    ]
    if previously_generated_metaphors:
        list_str = "\n".join(previously_generated_metaphors)
        return (
            "Do not repeat these previously generated metaphors. "
            "Also, do not be constrained to formula of the metaphors in the list. "
            "Make sure to balance the use of the various metaphor formulas given above:\n"
            f"{list_str}"
        )
    return ""


def save_metaphor(metaphor, metaphor_id, output_dir):
    filename = to_snake_case(metaphor.metaphor)
    data = metaphor.dict()
    timestr = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    data["timestamp"] = timestr
    metaphor_id_padded = str(metaphor_id).zfill(4)
    json_dump(data, f"{output_dir}/{metaphor_id_padded}_{filename}.json")


def generate_multiple_metaphors(output_dir=DEFAULT_METAPHORS_DIR, n=50):
    output_dir = ensure_dir(output_dir)
    metaphors = load_metaphors_data(output_dir)
    metaphor_agent = MetaphorAgent()
    max_id = get_metaphor_count(metaphors)
    for i in range(n):
        metaphors = load_metaphors_data(output_dir)

        previously_generated_metaphors = list_previous_metaphors(metaphors)
        rprint(previously_generated_metaphors)

        metaphor = metaphor_agent.propose_new_metaphor(
            previously_generated_metaphors=previously_generated_metaphors
        )
        rprint(metaphor)

        save_metaphor(metaphor, max_id + i + 1, output_dir)


def generate_single_metaphor(output_dir=DEFAULT_METAPHORS_DIR, metaphor_to_expand=None):
    output_dir = ensure_dir(output_dir)

    metaphor_agent = MetaphorAgent()
    metaphors = load_metaphors_data(output_dir)
    max_id = get_metaphor_count(metaphors)
    rprint(f"Max ID: {max_id}")

    if metaphor_to_expand:
        print(f"Expanding metaphor: {metaphor_to_expand}")
        metaphor = metaphor_agent.expand_given_metaphor(metaphor_to_expand)
    else:
        previously_generated_metaphors = list_previous_metaphors(metaphors)
        rprint(previously_generated_metaphors)
        metaphor = metaphor_agent.propose_new_metaphor(
            previously_generated_metaphors=previously_generated_metaphors
        )

    rprint(metaphor)
    save_metaphor(metaphor, max_id + 1, output_dir)


def parse_args():
    parser = argparse.ArgumentParser(description="Run the metaphor agent.")
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_METAPHORS_DIR,
        help="Directory where metaphor JSON files will be written.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="Generate this many new metaphors instead of expanding a preset list.",
    )
    parser.add_argument(
        "--expand",
        nargs="+",
        default=None,
        help="Expand one or more provided metaphor strings.",
    )
    parser.add_argument(
        "--metaphors-list-file",
        default=DEFAULT_METAPHORS_LIST_FILE,
        help="Text file containing one metaphor seed per line for the full run.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.expand:
        for metaphor_str in args.expand:
            generate_single_metaphor(
                output_dir=args.output_dir,
                metaphor_to_expand=metaphor_str,
            )
    elif args.count is not None:
        generate_multiple_metaphors(output_dir=args.output_dir, n=args.count)
    else:
        for metaphor_str in load_metaphors_to_expand(args.metaphors_list_file):
            generate_single_metaphor(
                output_dir=args.output_dir,
                metaphor_to_expand=metaphor_str,
            )
