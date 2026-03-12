from pathlib import Path


def load_prompt(prompt, ext="txt"):
    prompt_path = Path(__file__).resolve().parent / f"{prompt}.{ext}"
    return prompt_path.read_text(encoding="utf-8")
