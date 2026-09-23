# Reading Files & Listing Directories for Absolute Beginners

> How to open files, read them, and explore folders — explained like you're 10 years old.

---

## 1. The Real-World Analogy

Think of your computer as a **filing cabinet**:

```text
🗄️ Filing Cabinet (Your Computer)
   │
   ├── 📁 Drawer: "Documents"
   │      ├── 📄 resume.txt
   │      └── 📄 notes.md
   │
   ├── 📁 Drawer: "Photos"
   │      ├── 🖼️ vacation.jpg
   │      └── 🖼️ selfie.png
   │
   └── 📁 Drawer: "Projects"
          └── 📁 Sub-drawer: "my_app"
                 ├── 📄 app.py
                 └── 📄 config.json
```

Python gives you 3 simple actions:
1. **Open a drawer** and see what's inside → `os.listdir()` or `Path.iterdir()`
2. **Pick up a file** and read it → `open()` and `.read()`
3. **Write something** on a new file → `open()` and `.write()`

---

## 2. Reading a File (The 3-Line Version)

### The Absolute Simplest Way

```python
# 1. Open the file
# 2. Read the contents
# 3. Print it
with open("hello.txt") as f:
    content = f.read()
    print(content)
```

That's it. Three lines. Let's break it down:

```text
with open("hello.txt") as f:
 │     │       │         │
 │     │       │         └── f = nickname for the open file (like a bookmark)
 │     │       └──────────── the file you want to open
 │     └──────────────────── built-in function: "open this file"
 └────────────────────────── "with" = auto-closes the file when done (safety net)
```

### Why `with`?

Without `with`, you'd have to manually close the file:

```python
# Without "with" (risky, you might forget to close)
f = open("hello.txt")
content = f.read()
f.close()   # ← If you forget this, bad things can happen

# With "with" (safe, Python closes it for you automatically)
with open("hello.txt") as f:
    content = f.read()
# File is automatically closed here. No need to worry!
```

> **Rule:** Always use `with`. It's like a self-closing door.

---

## 3. The 4 Ways to Read a File

| Method | What it does | When to use |
| :--- | :--- | :--- |
| `.read()` | Reads the **entire file** as one big string | Small files |
| `.readline()` | Reads **one line** at a time | When you need just the first line |
| `.readlines()` | Reads **all lines** into a **list** | When you want to loop through lines |
| `for line in f:` | Reads **one line at a time** (memory-friendly) | Big files |

### Example: Read the entire file
```python
with open("hello.txt") as f:
    everything = f.read()
    print(everything)
```

### Example: Read line by line (best for big files)
```python
with open("hello.txt") as f:
    for line in f:
        print(line.strip())   # .strip() removes extra blank lines
```

### Example: Read all lines into a list
```python
with open("hello.txt") as f:
    lines = f.readlines()
    print(lines)
    # Output: ["Hello\n", "World\n", "Python\n"]
```

---

## 4. Writing to a File

### Create a new file (or overwrite)
```python
with open("output.txt", "w") as f:    # "w" = write mode
    f.write("Hello World!\n")
    f.write("Python is awesome!\n")
```

### Add to an existing file (append)
```python
with open("output.txt", "a") as f:    # "a" = append mode
    f.write("This line is added at the end.\n")
```

### The mode cheat sheet
| Mode | Meaning | What happens if file exists? | What happens if file doesn't exist? |
| :--- | :--- | :--- | :--- |
| `"r"` | Read (default) | Opens it | Error! |
| `"w"` | Write | **Overwrites everything!** | Creates it |
| `"a"` | Append | Adds to the end | Creates it |
| `"x"` | Create only | Error! (won't overwrite) | Creates it |

---

## 5. Listing Files in a Directory

### Method 1: `os.listdir()` — The Simple Way

```python
import os

# List everything in the current folder
files = os.listdir(".")
print(files)
# Output: ['app.py', 'data', 'config.json', 'README.md']
```

```text
os.listdir(".")
    │         │
    │         └── "." means "this folder" (current directory)
    └──────────── "list the contents of this directory"
```

### Method 2: `os.listdir()` with a specific path

```python
import os

files = os.listdir("/home/santosh/Documents")
for f in files:
    print(f)
```

### Method 3: `pathlib.Path` — The Modern Way (Recommended!)

```python
from pathlib import Path

folder = Path(".")   # Current directory

for item in folder.iterdir():
    print(item.name, "→", "📁 Folder" if item.is_dir() else "📄 File")
```

Output:
```text
app.py → 📄 File
data → 📁 Folder
config.json → 📄 File
README.md → 📄 File
```

---

## 6. Finding Specific Files (Filtering)

### Find only `.txt` files
```python
from pathlib import Path

for f in Path(".").glob("*.txt"):
    print(f.name)
```

### Find only `.py` files in all subfolders (recursive)
```python
from pathlib import Path

for f in Path(".").rglob("*.py"):    # rglob = recursive glob
    print(f)
```

### Filter with `os.listdir()`
```python
import os

all_files = os.listdir(".")
txt_files = [f for f in all_files if f.endswith(".txt")]
print(txt_files)
```

---

## 7. Checking If a File or Folder Exists

```python
from pathlib import Path

# Does the file exist?
if Path("config.json").exists():
    print("Found it!")
else:
    print("File not found!")

# Is it a file or a folder?
p = Path("data")
print(p.is_file())     # False (it's a folder)
print(p.is_dir())      # True
```

With `os`:
```python
import os

os.path.exists("config.json")     # True or False
os.path.isfile("config.json")     # True if it's a file
os.path.isdir("data")             # True if it's a folder
```

---

## 8. Getting File Information

```python
from pathlib import Path

f = Path("hello.txt")

print(f.name)        # "hello.txt"         (just the filename)
print(f.stem)        # "hello"             (name without extension)
print(f.suffix)      # ".txt"              (just the extension)
print(f.parent)      # "."                 (the folder it's in)
print(f.stat().st_size)  # 1234            (size in bytes)
```

---

## 9. `os` vs `pathlib` — Which One Should I Use?

| Feature | `os` (Old Way) | `pathlib` (Modern Way) |
| :--- | :--- | :--- |
| **Style** | Functions with strings | Object-oriented (uses `.`) |
| **Readability** | `os.path.join("a", "b")` | `Path("a") / "b"` |
| **List directory** | `os.listdir(".")` | `Path(".").iterdir()` |
| **Find files** | Manual filtering | `Path(".").glob("*.txt")` |
| **Recommended?** | Works, but older style | ✅ **Yes, use this!** |

> **For beginners:** Use `pathlib`. It reads like English.

---

## 10. Complete Working Examples

### Example A: Read a file and count lines

```python
from pathlib import Path

file_path = Path("hello.txt")

if file_path.exists():
    content = file_path.read_text()
    lines = content.strip().split("\n")
    print(f"The file has {len(lines)} lines.")
else:
    print("File not found!")
```

### Example B: List all Python files in a project

```python
from pathlib import Path

project = Path(".")

print("Python files in this project:")
for py_file in project.rglob("*.py"):
    size_kb = py_file.stat().st_size / 1024
    print(f"  📄 {py_file} ({size_kb:.1f} KB)")
```

### Example C: Read all `.txt` files in a folder

```python
from pathlib import Path

folder = Path("emails")

for txt_file in folder.glob("*.txt"):
    print(f"\n--- {txt_file.name} ---")
    print(txt_file.read_text())
```

---

## 11. Quick Reference Cheat Sheet

| What You Want | `pathlib` (Modern) | `os` (Classic) |
| :--- | :--- | :--- |
| **Read entire file** | `Path("f.txt").read_text()` | `open("f.txt").read()` |
| **Write to file** | `Path("f.txt").write_text("hi")` | `open("f.txt","w").write("hi")` |
| **List a directory** | `Path(".").iterdir()` | `os.listdir(".")` |
| **Find by pattern** | `Path(".").glob("*.py")` | Manual filter with `endswith` |
| **Find recursively** | `Path(".").rglob("*.py")` | `os.walk()` (complicated) |
| **Check if exists** | `Path("f.txt").exists()` | `os.path.exists("f.txt")` |
| **Is it a file?** | `Path("f").is_file()` | `os.path.isfile("f")` |
| **Is it a folder?** | `Path("d").is_dir()` | `os.path.isdir("d")` |
| **Get filename** | `Path("a/b.txt").name` | `os.path.basename("a/b.txt")` |
| **Get extension** | `Path("b.txt").suffix` | `os.path.splitext("b.txt")[1]` |
| **Join paths** | `Path("a") / "b" / "c.txt"` | `os.path.join("a","b","c.txt")` |

---

## 12. How It Connects to Everything Else

Remember the universal pattern?

```text
from [toolbox] import [Blueprint]
tool = Blueprint(settings)
result = tool.do_something()
```

File operations follow the exact same model:

```text
ARGPARSE                    OPENAI                      PATHLIB
────────                    ──────                      ───────
from argparse import ...    from openai import OpenAI   from pathlib import Path
parser = ArgumentParser()   client = OpenAI()           folder = Path(".")
args = parser.parse_args()  resp = client...create()    files = folder.glob("*.py")
print(args.name)            print(resp...content)       for f in files: print(f)
```

Same mental model. Different toolbox. 🚀
