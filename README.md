# Python Basics

A repository dedicated to learning and mastering Python fundamentals, concepts, and standard library modules with beginner-friendly guides, easy helper libraries, and runnable examples.

## 📚 Guides (For Absolute Beginners)

- 🧠 [**Python Concepts for Absolute Dummies**](python_concepts_for_dummies.md): What is a Class, Object, Method, `__init__`, `self`, built-in functions (`print`, `len`, `type`), dunder methods — explained with zero jargon.
- 📁 [**Files & Directories for Beginners**](files_beginner.md): How to read files, write data, list folders, and explore directories using the filing cabinet analogy.
- 🧰 [**Argparse for Beginners**](argparse_beginner.md): Visual mental models, flowcharts, the "Toolbox Analogy", and a copy-paste CLI template.
- 🤖 [**OpenAI SDK for Beginners**](openai_beginner.md): From `from openai import OpenAI` to calling GPT-4o and Ollama — explained with the Swiggy/Zomato food delivery analogy.

---

## 🛠️ Included Beginner Libraries

### `easyfile.py` — Dead Simple File & Folder Manager
Made for absolute dummies who don't want to deal with complex `os` or `pathlib` quirks.

```python
import easyfile

# Read a file in 1 line
text = easyfile.read("notes.txt")

# Read line by line as a list
lines = easyfile.read_lines("notes.txt")

# Write or append text
easyfile.write("hello.txt", "Hello World!")
easyfile.append("log.txt", "New entry\n")

# List folders with nice icons
easyfile.list_files_pretty(".")

# Find specific files
py_files = easyfile.find_files(".", "*.py")

# Get file info (size, extension, path)
easyfile.file_info_pretty("hello.txt")
```

---

## 💻 Runnable Examples

| # | File | What It Teaches |
| :--- | :--- | :--- |
| 01 | [`01_simple_argparse.py`](examples/01_simple_argparse.py) | Positional arguments, optional flags, types, and defaults |
| 02 | [`02_class_and_method.py`](examples/02_class_and_method.py) | Initializing a Python class and calling its methods via CLI |
| 03 | [`03_openai_simple.py`](examples/03_openai_simple.py) | Ask OpenAI a question from the terminal using argparse + OpenAI SDK |
| 04 | [`04_openai_classifier.py`](examples/04_openai_classifier.py) | Classify text into categories with structured JSON output |
| 05 | [`05_read_and_list_files.py`](examples/05_read_and_list_files.py) | Read, write, and list directories using the beginner-friendly `easyfile` library |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/santosh91parsa/Pythonbasics.git
cd Pythonbasics

# 1. Test the easyfile library (zero dependencies needed)
python easyfile.py
python examples/05_read_and_list_files.py

# 2. Try CLI arguments (no API key needed)
python examples/01_simple_argparse.py Alice --sugar 3 --iced

# 3. Try OpenAI (requires API key)
export OPENAI_API_KEY="sk-your-key"
python examples/03_openai_simple.py "What is Docker?"
```
