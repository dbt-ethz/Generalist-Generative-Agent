import argparse
import os
from pathlib import Path

import pandas as pd
from PIL import Image

from ria.agents import EvaluationAgent, EvaluationModel
from ria.utils import json_load


ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_DATA_DIR = ROOT_DIR / "output" / "experiment_data" / "03_designs_H_gpt-4o"
DEFAULT_EVAL_CROPS_DIR = ROOT_DIR / "output" / "evaluation_crops"


def parse_args():
    parser = argparse.ArgumentParser(description="Run the evaluation agent on rendered design folders.")
    parser.add_argument(
        "--data-dir",
        default=str(DEFAULT_DATA_DIR),
        help="Root directory containing rendered design folders with PNG files.",
    )
    parser.add_argument(
        "--eval-crops-dir",
        default=str(DEFAULT_EVAL_CROPS_DIR),
        help="Directory where cropped evaluation images will be written.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of design folders to evaluate.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Recompute evaluation.csv even if it already exists.",
    )
    return parser.parse_args()


def add_averages(df):
    score_columns = list(EvaluationModel.schema()["properties"].keys())
    averages = df[score_columns].mean()
    average_row = {"image_path": "overall", **averages.to_dict()}
    df = pd.concat([df, pd.DataFrame([average_row])], ignore_index=True)
    df["average"] = df[score_columns].mean(axis=1)
    return df


def build_items_dict(data_dir):
    folder_dict = {}
    for root, _, files in os.walk(data_dir):
        png_list = sorted(
            os.path.join(root, file) for file in files if file.lower().endswith(".png")
        )
        json_files = sorted(
            os.path.join(root, file)
            for file in files
            if file.lower().endswith(".json") and file != "progress_log.json"
        )
        if png_list:
            folder_dict[root] = {"images_list": png_list, "json_files": json_files}
    return dict(sorted(folder_dict.items()))


def is_placeholder_image(image):
    rgb_image = image.convert("RGB")
    extrema = rgb_image.getextrema()
    min_threshold = 55
    max_threshold = 68
    return all(
        min_threshold <= channel_min <= max_threshold
        and min_threshold <= channel_max <= max_threshold
        for channel_min, channel_max in extrema
    )


def crop_for_evaluation(image):
    width, height = image.size
    if width >= 896 and height >= 986:
        return image.crop((384, 474, 896, 986))

    crop_size = min(width, height, 512)
    left = max((width - crop_size) // 2, 0)
    top = max((height - crop_size) // 2, 0)
    right = left + crop_size
    bottom = top + crop_size
    return image.crop((left, top, right, bottom))


def evaluate_folder(agent, folder, content, data_dir, eval_crops_dir):
    if not content.get("json_files"):
        with open(os.path.join(folder, "evaluation.csv"), "w") as handle:
            handle.write("None")
        return

    metaphor_data = json_load(content["json_files"][0])
    columns = ["image_path"] + list(EvaluationModel.schema()["properties"].keys())
    evaluation_results = pd.DataFrame(columns=columns)

    for image_file in content["images_list"]:
        print(f"Evaluating image: {image_file}")
        with Image.open(image_file) as image:
            if is_placeholder_image(image):
                print(f"Skipping placeholder image: {image_file}")
                evaluation = EvaluationModel(
                    metaphor_alignment_score=None,
                    conceptual_strength_score=None,
                    geometric_complexity_score=None,
                    design_task_adherence_score=None,
                )
            else:
                cropped_image = crop_for_evaluation(image)
                new_image_path = image_file.replace(data_dir, eval_crops_dir)
                os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
                cropped_image.save(new_image_path)
                print(f"Saved crop: {new_image_path}")
                evaluation = agent.evaluate_architectural_model(
                    new_image_path, metaphor_data
                )
                print(evaluation)

        new_row = pd.DataFrame(
            [{"image_path": image_file, **evaluation.dict()}]
        )
        evaluation_results = pd.concat(
            [evaluation_results, new_row], ignore_index=True
        )

    evaluation_results = add_averages(evaluation_results)
    evaluation_results["metaphor_file_path"] = content["json_files"][0]
    evaluation_results.to_csv(os.path.join(folder, "evaluation.csv"), index=False)


def main():
    args = parse_args()
    data_dir = str(Path(args.data_dir).resolve())
    eval_crops_dir = str(Path(args.eval_crops_dir).resolve())

    if not os.path.isdir(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    folders_to_evaluate = list(build_items_dict(data_dir).items())
    if args.limit is not None:
        folders_to_evaluate = folders_to_evaluate[: args.limit]

    if not folders_to_evaluate:
        raise FileNotFoundError(f"No rendered design folders found under: {data_dir}")

    agent = EvaluationAgent()
    evaluated_count = 0

    for folder, content in folders_to_evaluate:
        if not args.overwrite and os.path.exists(os.path.join(folder, "evaluation.csv")):
            print(f"Skipping existing evaluation: {folder}")
            continue

        print(f"Folder: {folder}")
        evaluate_folder(agent, folder, content, data_dir, eval_crops_dir)
        evaluated_count += 1

    print(f"Evaluation complete. Evaluated {evaluated_count} folder(s).")


if __name__ == "__main__":
    main()
