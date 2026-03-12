import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT_DIR = ROOT_DIR / "output" / "experiment_data" / "03_designs_H_gpt-4o"
DEFAULT_SCENE_FILE = ROOT_DIR / "ria" / "visualization" / "230125_render_enviroment.blend"
DEFAULT_BATCH_SCRIPT = ROOT_DIR / "ria" / "visualization" / "batch_ops.py"
BLENDER_ENV_VAR = "BLENDER_BIN"


def parse_args():
    parser = argparse.ArgumentParser(description="Run batch Blender renders for GH outputs.")
    parser.add_argument(
        "--input-dir",
        default=str(DEFAULT_INPUT_DIR),
        help="Root directory containing GH output folders, or a single design folder with OBJ files.",
    )
    parser.add_argument(
        "--scene-file",
        default=str(DEFAULT_SCENE_FILE),
        help="Blender scene file to open for rendering.",
    )
    parser.add_argument(
        "--blender-bin",
        default=None,
        help=f"Explicit Blender executable. Overrides {BLENDER_ENV_VAR} and auto-detection.",
    )
    parser.add_argument(
        "--render-style",
        default="GHOSTED",
        choices=["SOLID", "GHOSTED", "WIREFRAME"],
        help="Render style to request from the Blender batch script.",
    )
    parser.add_argument(
        "--resolution-x",
        type=int,
        default=1280,
        help="Render width in pixels.",
    )
    parser.add_argument(
        "--resolution-y",
        type=int,
        default=1280,
        help="Render height in pixels.",
    )
    parser.add_argument(
        "--samples",
        type=int,
        default=300,
        help="Cycles sample count.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-render images even if they already exist.",
    )
    parser.add_argument(
        "--y-up",
        action="store_true",
        help="Import OBJ files as Y-up instead of Z-up.",
    )
    parser.add_argument(
        "--global-scale",
        action="store_true",
        help="Use one shared scale factor across all variants in a design folder.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Maximum number of design folders to render.",
    )
    parser.add_argument(
        "--show-ui",
        action="store_true",
        help="Launch Blender with its UI instead of background mode.",
    )
    return parser.parse_args()


def blender_candidates():
    seen = set()
    candidates = []

    def add(candidate):
        if not candidate:
            return
        candidate = str(candidate)
        if candidate in seen:
            return
        seen.add(candidate)
        candidates.append(Path(candidate))

    add(os.getenv(BLENDER_ENV_VAR))

    system = platform.system()
    if system == "Darwin":
        add("/Applications/Blender 3.6.app/Contents/MacOS/blender")
        add(str(Path.home() / "Applications" / "Blender 3.6.app" / "Contents" / "MacOS" / "blender"))
    elif system == "Windows":
        program_files = os.environ.get("ProgramFiles", r"C:\Program Files")
        add(Path(program_files) / "Blender Foundation" / "Blender 3.6" / "blender.exe")
    else:
        add("/usr/bin/blender")
        add("/usr/local/bin/blender")
        add("/snap/bin/blender")

    add(shutil.which("blender"))
    return candidates


def blender_version(blender_bin):
    try:
        result = subprocess.run(
            [str(blender_bin), "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None

    output = "\n".join(part for part in [result.stdout, result.stderr] if part)
    match = re.search(r"Blender\s+(\d+\.\d+(?:\.\d+)?)", output)
    if match:
        return match.group(1)
    return None


def find_blender_bin(explicit_path=None):
    mismatched_versions = []
    candidates = [Path(explicit_path)] if explicit_path else blender_candidates()

    for candidate in candidates:
        if not candidate or not candidate.exists():
            continue
        version = blender_version(candidate)
        if version is None:
            continue
        if version.startswith("3.6"):
            return candidate, version
        mismatched_versions.append((candidate, version))

    if explicit_path:
        raise FileNotFoundError(
            f"Blender 3.6 was not found at the requested path: {explicit_path}"
        )

    mismatch_summary = ", ".join(f"{path} ({version})" for path, version in mismatched_versions)
    if mismatch_summary:
        raise RuntimeError(
            "Found Blender executables, but none are version 3.6. "
            f"Detected: {mismatch_summary}. "
            f"Install Blender 3.6 or set {BLENDER_ENV_VAR} / --blender-bin to the 3.6 executable."
        )

    raise FileNotFoundError(
        "Blender 3.6 was not found. Install Blender 3.6 or set "
        f"{BLENDER_ENV_VAR} / --blender-bin to the Blender 3.6 executable."
    )


def validate_paths(scene_file, input_dir):
    scene_path = Path(scene_file)
    input_path = Path(input_dir)

    if not scene_path.exists():
        raise FileNotFoundError(f"Blender scene file not found: {scene_path}")
    if not DEFAULT_BATCH_SCRIPT.exists():
        raise FileNotFoundError(f"Blender batch script not found: {DEFAULT_BATCH_SCRIPT}")
    if not input_path.exists():
        raise FileNotFoundError(f"Render input directory not found: {input_path}")

    return scene_path, input_path


def build_command(blender_bin, scene_file, args):
    command = [str(blender_bin), str(scene_file)]
    if not args.show_ui:
        command.append("--background")
    command.extend(
        [
            "--python",
            str(DEFAULT_BATCH_SCRIPT),
            "--",
            "--input-dir",
            str(Path(args.input_dir).resolve()),
            "--render-style",
            args.render_style,
            "--resolution-x",
            str(args.resolution_x),
            "--resolution-y",
            str(args.resolution_y),
            "--samples",
            str(args.samples),
        ]
    )

    if args.overwrite:
        command.append("--overwrite")
    if args.y_up:
        command.append("--y-up")
    if args.global_scale:
        command.append("--global-scale")
    if args.limit is not None:
        command.extend(["--limit", str(args.limit)])

    return command


def main():
    args = parse_args()
    scene_file, _ = validate_paths(args.scene_file, args.input_dir)
    blender_bin, blender_version_str = find_blender_bin(args.blender_bin)

    print(f"Using Blender {blender_version_str}: {blender_bin}")
    print(f"Using scene file: {scene_file}")
    print(f"Rendering input: {Path(args.input_dir).resolve()}")

    command = build_command(blender_bin, scene_file, args)
    print("Launching Blender batch render...")
    subprocess.run(command, check=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        sys.exit(exc.returncode)
