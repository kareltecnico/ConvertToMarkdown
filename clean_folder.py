from pathlib import Path
import argparse

PROTECTED_FILENAMES = {"README.md"}


def clean_folder(folder: Path) -> tuple[int, int]:
    deleted = 0
    failed = 0

    folder.mkdir(exist_ok=True)

    for path in sorted(folder.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if path.name.startswith(".") or path.name in PROTECTED_FILENAMES:
            continue

        try:
            if path.is_file() or path.is_symlink():
                path.unlink()
                deleted += 1
            elif path.is_dir() and not any(path.iterdir()):
                path.rmdir()
        except Exception as e:
            print(f"  [ERROR] Could not delete {path}: {e}")
            failed += 1

    return deleted, failed


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean ConvertToMarkdown folders.")
    parser.add_argument("folder", choices=("input", "output"))
    args = parser.parse_args()

    folder = Path(args.folder)
    print(f"Cleaning {folder.resolve()}")
    deleted, failed = clean_folder(folder)
    print(f"Deleted: {deleted}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()
