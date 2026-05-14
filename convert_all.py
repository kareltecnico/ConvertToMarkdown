from pathlib import Path
from markitdown import MarkItDown

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(exist_ok=True)

pdf_files = list(INPUT_DIR.glob("*.pdf"))

if not pdf_files:
    print("No PDF files found in input folder.")
    exit()

md = MarkItDown()

success_count = 0
fail_count = 0

for pdf in pdf_files:
    output_file = OUTPUT_DIR / f"{pdf.stem}.md"
    print(f"Converting: {pdf.name}")

    try:
        result = md.convert(str(pdf))
        content = result.text_content

        if not content or not content.strip():
            print(f"  [WARNING] Empty output for: {pdf.name}")
            fail_count += 1
            continue

        output_file.write_text(content, encoding="utf-8")
        print(f"  [OK] Saved: {output_file.name}")
        success_count += 1

    except Exception as e:
        print(f"  [ERROR] Failed to convert {pdf.name}: {e}")
        fail_count += 1

print(f"\nDone: {success_count} converted, {fail_count} failed.")