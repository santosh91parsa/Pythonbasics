"""
Example 5: Read files and list directories using easyfile (made for beginners)
Run with:
    python examples/05_read_and_list_files.py
"""
import sys
import os

# Add parent directory to path so we can import easyfile
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import easyfile

def main():
    print("\n--- 1. List Everything in the Current Folder ---")
    easyfile.list_files_pretty(".")

    print("\n--- 2. Write a Simple Note ---")
    note_content = (
        "Shopping List:\n"
        "1. Apples\n"
        "2. Milk\n"
        "3. Coffee beans\n"
    )
    easyfile.write("my_notes.txt", note_content)

    print("\n--- 3. Read the Note Back (Full Text) ---")
    text = easyfile.read("my_notes.txt")
    print(text)

    print("\n--- 4. Read Line by Line ---")
    lines = easyfile.read_lines("my_notes.txt")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line}")

    print("\n--- 5. Get File Information (Size, Path, Type) ---")
    easyfile.file_info_pretty("my_notes.txt")

    print("\n--- 6. Find All Markdown (.md) Files ---")
    md_files = easyfile.find_files(".", "*.md")
    print(f"Found {len(md_files)} markdown files:")
    for f in md_files:
        print(f"  📄 {f.name}")

    # Cleanup the test note
    if os.path.exists("my_notes.txt"):
        os.remove("my_notes.txt")
        print("\n🧹 Cleaned up my_notes.txt demo file.")

if __name__ == "__main__":
    main()
