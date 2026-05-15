from pathlib import Path
from datetime import datetime
import warnings

warnings.filterwarnings(
    "ignore",
    message="Couldn't find ffmpeg or avconv.*",
    category=RuntimeWarning,
)

from markitdown import MarkItDown

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
REPORT_FILE = OUTPUT_DIR / "conversion_report.txt"
SKIP_FILENAMES = {"README.md"}
SKIP_EXTENSIONS = {".md"}


def is_convertible_file(path: Path) -> bool:
    return (
        path.is_file()
        and not path.name.startswith(".")
        and path.name not in SKIP_FILENAMES
        and path.suffix.lower() not in SKIP_EXTENSIONS
    )


def discover_input_files() -> list[Path]:
    return sorted(
        (file for file in INPUT_DIR.rglob("*") if is_convertible_file(file)),
        key=lambda file: file.relative_to(INPUT_DIR).as_posix().lower(),
    )


def build_output_paths(input_files: list[Path]) -> dict[Path, Path]:
    relative_stems = {}

    for input_file in input_files:
        relative_stem = input_file.relative_to(INPUT_DIR).with_suffix("")
        relative_stems[relative_stem] = relative_stems.get(relative_stem, 0) + 1

    output_paths = {}
    for input_file in input_files:
        relative_stem = input_file.relative_to(INPUT_DIR).with_suffix("")
        if relative_stems[relative_stem] > 1:
            suffix = input_file.suffix.lower().lstrip(".")
            relative_output = relative_stem.with_name(f"{relative_stem.name}-{suffix}.md")
        else:
            relative_output = relative_stem.with_suffix(".md")

        output_paths[input_file] = OUTPUT_DIR / relative_output

    return output_paths


def should_skip(input_file: Path, output_file: Path) -> bool:
    return output_file.exists() and output_file.stat().st_mtime >= input_file.stat().st_mtime


def write_report(entries: list[str], converted: int, skipped: int, failed: int) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "ConvertToMarkdown conversion report",
        f"Generated: {timestamp}",
        f"Input: {INPUT_DIR.resolve()}",
        f"Output: {OUTPUT_DIR.resolve()}",
        "",
        f"Converted: {converted}",
        f"Skipped: {skipped}",
        f"Failed: {failed}",
        "",
        "Details:",
        *entries,
        "",
    ]
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    input_files = discover_input_files()
    if not input_files:
        print("No supported input files found in input folder.")
        return

    md = MarkItDown()
    output_paths = build_output_paths(input_files)
    report_entries = []
    converted_count = 0
    skipped_count = 0
    fail_count = 0

    for input_file in input_files:
        relative_input = input_file.relative_to(INPUT_DIR)
        output_file = output_paths[input_file]
        relative_output = output_file.relative_to(OUTPUT_DIR)

        if should_skip(input_file, output_file):
            print(f"Skipping unchanged: {relative_input}")
            report_entries.append(f"[SKIPPED] {relative_input} -> {relative_output}")
            skipped_count += 1
            continue

        print(f"Converting: {relative_input}")

        try:
            result = md.convert_local(str(input_file))
            content = result.text_content

            if not content or not content.strip():
                print(f"  [WARNING] Empty output for: {relative_input}")
                report_entries.append(f"[WARNING] {relative_input} -> empty output")
                fail_count += 1
                continue

            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(content, encoding="utf-8")
            print(f"  [OK] Saved: {relative_output}")
            report_entries.append(f"[OK] {relative_input} -> {relative_output}")
            converted_count += 1

        except Exception as e:
            print(f"  [ERROR] Failed to convert {relative_input}: {e}")
            report_entries.append(f"[ERROR] {relative_input} -> {e}")
            fail_count += 1

    write_report(report_entries, converted_count, skipped_count, fail_count)

    print("")
    print(f"Converted: {converted_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Failed: {fail_count}")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")
    print(f"Report: {REPORT_FILE.resolve()}")


if __name__ == "__main__":
    main()
