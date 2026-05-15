from pathlib import Path
import warnings

warnings.filterwarnings(
    "ignore",
    message="Couldn't find ffmpeg or avconv.*",
    category=RuntimeWarning,
)

from markitdown import MarkItDown

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
SKIP_FILENAMES = {"README.md"}
SKIP_EXTENSIONS = {".md"}

OUTPUT_DIR.mkdir(exist_ok=True)

input_files = sorted(
    file
    for file in INPUT_DIR.iterdir()
    if file.is_file()
    and not file.name.startswith(".")
    and file.name not in SKIP_FILENAMES
    and file.suffix.lower() not in SKIP_EXTENSIONS
)

if not input_files:
    print("No supported input files found in input folder.")
    exit()

md = MarkItDown()

success_count = 0
fail_count = 0
stem_counts = {}

for input_file in input_files:
    stem_counts[input_file.stem] = stem_counts.get(input_file.stem, 0) + 1


def output_path_for(input_file: Path) -> Path:
    if stem_counts[input_file.stem] > 1:
        suffix = input_file.suffix.lower().lstrip(".")
        return OUTPUT_DIR / f"{input_file.stem}-{suffix}.md"

    return OUTPUT_DIR / f"{input_file.stem}.md"


for input_file in input_files:
    output_file = output_path_for(input_file)
    print(f"Converting: {input_file.name}")

    try:
        result = md.convert_local(str(input_file))
        content = result.text_content

        if not content or not content.strip():
            print(f"  [WARNING] Empty output for: {input_file.name}")
            fail_count += 1
            continue

        output_file.write_text(content, encoding="utf-8")
        print(f"  [OK] Saved: {output_file.name}")
        success_count += 1

    except Exception as e:
        print(f"  [ERROR] Failed to convert {input_file.name}: {e}")
        fail_count += 1

print(f"\nDone: {success_count} converted, {fail_count} failed.")
