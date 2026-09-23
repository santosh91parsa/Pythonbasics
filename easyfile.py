"""
easyfile.py — A dead-simple file utility library for beginners.

No confusing APIs. Just plain English function names.
Import this file and use it like a TV remote.

Usage:
    from easyfile import read, write, list_files, find_files, file_info

Author: Santosh Parsa
"""
from pathlib import Path


# ============================================================
# 1. READ A FILE
# ============================================================

def read(filepath):
    """
    Read an entire file and return its content as a string.

    Example:
        content = read("hello.txt")
        print(content)
    """
    p = Path(filepath)
    if not p.exists():
        print(f"❌ File not found: {filepath}")
        return None
    if not p.is_file():
        print(f"❌ Not a file (it's a folder): {filepath}")
        return None
    return p.read_text()


def read_lines(filepath):
    """
    Read a file and return each line as a list.

    Example:
        lines = read_lines("data.txt")
        for line in lines:
            print(line)
    """
    content = read(filepath)
    if content is None:
        return []
    return content.strip().split("\n")


# ============================================================
# 2. WRITE TO A FILE
# ============================================================

def write(filepath, content):
    """
    Write content to a file (creates or overwrites).

    Example:
        write("output.txt", "Hello World!")
    """
    Path(filepath).write_text(content)
    print(f"✅ Written to {filepath}")


def append(filepath, content):
    """
    Add content to the end of a file.

    Example:
        append("log.txt", "New log entry\\n")
    """
    with open(filepath, "a") as f:
        f.write(content)
    print(f"✅ Appended to {filepath}")


# ============================================================
# 3. LIST FILES IN A DIRECTORY
# ============================================================

def list_files(directory="."):
    """
    List all files and folders in a directory.
    Returns a list of names.

    Example:
        files = list_files(".")
        for f in files:
            print(f)
    """
    p = Path(directory)
    if not p.exists():
        print(f"❌ Directory not found: {directory}")
        return []
    if not p.is_dir():
        print(f"❌ Not a directory: {directory}")
        return []

    items = []
    for item in sorted(p.iterdir()):
        icon = "📁" if item.is_dir() else "📄"
        items.append({"name": item.name, "type": "folder" if item.is_dir() else "file", "icon": icon})

    return items


def list_files_pretty(directory="."):
    """
    List all files and folders in a directory with pretty formatting.

    Example:
        list_files_pretty("/home/santosh/projects")
    """
    items = list_files(directory)
    if not items:
        return

    print(f"\n📂 Contents of: {Path(directory).resolve()}")
    print("─" * 50)
    for item in items:
        print(f"  {item['icon']} {item['name']}")
    print("─" * 50)
    folders = sum(1 for i in items if i["type"] == "folder")
    files = sum(1 for i in items if i["type"] == "file")
    print(f"  {folders} folder(s), {files} file(s)\n")


# ============================================================
# 4. FIND FILES BY PATTERN
# ============================================================

def find_files(directory=".", pattern="*", recursive=False):
    """
    Find files matching a pattern (e.g., "*.txt", "*.py").

    Example:
        # Find all .py files in current folder
        py_files = find_files(".", "*.py")

        # Find all .txt files in all subfolders
        txt_files = find_files(".", "*.txt", recursive=True)
    """
    p = Path(directory)
    if not p.exists():
        print(f"❌ Directory not found: {directory}")
        return []

    if recursive:
        matches = list(p.rglob(pattern))
    else:
        matches = list(p.glob(pattern))

    # Return only files, not folders
    return [f for f in matches if f.is_file()]


# ============================================================
# 5. FILE INFO
# ============================================================

def file_info(filepath):
    """
    Get useful information about a file.

    Example:
        info = file_info("app.py")
        print(info)
    """
    p = Path(filepath)
    if not p.exists():
        print(f"❌ File not found: {filepath}")
        return None

    size_bytes = p.stat().st_size
    if size_bytes < 1024:
        size_str = f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.1f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.1f} MB"

    return {
        "name": p.name,
        "extension": p.suffix,
        "name_without_ext": p.stem,
        "folder": str(p.parent),
        "full_path": str(p.resolve()),
        "size": size_str,
        "size_bytes": size_bytes,
        "is_file": p.is_file(),
        "is_folder": p.is_dir(),
    }


def file_info_pretty(filepath):
    """
    Print file information in a readable format.

    Example:
        file_info_pretty("app.py")
    """
    info = file_info(filepath)
    if not info:
        return

    print(f"\n📄 File Info: {info['name']}")
    print("─" * 40)
    print(f"  Name       : {info['name']}")
    print(f"  Extension  : {info['extension']}")
    print(f"  Size       : {info['size']}")
    print(f"  Folder     : {info['folder']}")
    print(f"  Full Path  : {info['full_path']}")
    print("─" * 40 + "\n")


# ============================================================
# DEMO: Run this file directly to see it in action
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  📚 easyfile.py — Quick Demo")
    print("=" * 50)

    # Demo 1: List files
    list_files_pretty(".")

    # Demo 2: Find Python files
    py_files = find_files(".", "*.py")
    if py_files:
        print("🐍 Python files found:")
        for f in py_files:
            print(f"   {f}")

    # Demo 3: File info
    py_files = find_files(".", "*.py")
    if py_files:
        file_info_pretty(str(py_files[0]))

    # Demo 4: Write and read
    write("_demo_test.txt", "Hello from easyfile!\nLine 2\nLine 3")
    lines = read_lines("_demo_test.txt")
    print(f"📄 Read back {len(lines)} lines: {lines}")

    # Cleanup
    Path("_demo_test.txt").unlink()
    print("🗑️  Cleaned up demo file.\n")
