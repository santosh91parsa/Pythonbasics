# Python Basics

A repository dedicated to learning and mastering Python fundamentals, concepts, and standard library modules with beginner-friendly guides and runnable examples.

## 📚 Guides

- 🧠 [**Python Concepts for Absolute Dummies**](python_concepts_for_dummies.md): What is a Class, Object, Method, `__init__`, `self`, built-in functions, dunder methods — explained with zero jargon.
- 🧰 [**Argparse for Beginners**](argparse_beginner.md): Visual mental models, flowcharts, the "Toolbox Analogy", and a copy-paste starter template.
- 🤖 [**OpenAI SDK for Beginners**](openai_beginner.md): From `from openai import OpenAI` to calling GPT-4o and Ollama — with the Swiggy/Zomato delivery analogy.

## 💻 Runnable Examples

| # | File | What It Teaches |
| :--- | :--- | :--- |
| 01 | [`01_simple_argparse.py`](examples/01_simple_argparse.py) | Positional arguments, optional flags, types, and defaults |
| 02 | [`02_class_and_method.py`](examples/02_class_and_method.py) | Initializing a Python class and calling its methods via CLI |
| 03 | [`03_openai_simple.py`](examples/03_openai_simple.py) | Ask OpenAI a question from the terminal using argparse + OpenAI SDK |
| 04 | [`04_openai_classifier.py`](examples/04_openai_classifier.py) | Classify text into categories with structured JSON output |

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/santosh91parsa/Pythonbasics.git
cd Pythonbasics

# Try argparse (no API key needed)
python examples/01_simple_argparse.py Alice --sugar 3 --iced

# Try OpenAI (requires API key)
export OPENAI_API_KEY="sk-your-key"
python examples/03_openai_simple.py "What is Docker?"
```
