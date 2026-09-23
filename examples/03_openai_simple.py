"""
Example 3: Ask OpenAI a simple question
Run with:
    export OPENAI_API_KEY="sk-your-key"
    python examples/03_openai_simple.py "What is Docker?"
    python examples/03_openai_simple.py "Explain Kubernetes in one sentence"
"""
import argparse
from openai import OpenAI


def main():
    # Reusing argparse! (See argparse_beginner.md)
    parser = argparse.ArgumentParser(description="Ask OpenAI a question")
    parser.add_argument("question", help="Your question for the AI")
    parser.add_argument("--model", default="gpt-4o-mini", help="Model to use")
    args = parser.parse_args()

    # 1. Build the tool (Object from Class)
    client = OpenAI()

    # 2. Press the button (Method)
    response = client.chat.completions.create(
        model=args.model,
        messages=[
            {"role": "user", "content": args.question}
        ]
    )

    # 3. Read the delivery
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
