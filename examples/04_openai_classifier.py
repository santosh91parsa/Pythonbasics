"""
Example 4: Classify text using OpenAI (structured JSON output)
Run with:
    export OPENAI_API_KEY="sk-your-key"
    python examples/04_openai_classifier.py "You won a free iPhone! Click here!"
    python examples/04_openai_classifier.py "Hi team, let's meet at 2pm for the Q3 review."
"""
import argparse
import json
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="Classify text using AI")
    parser.add_argument("text", help="Text to classify")
    args = parser.parse_args()

    # 1. Build the client
    client = OpenAI()

    # 2. Ask the AI to classify (with JSON output)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a text classifier. Return valid JSON with keys: category, confidence, reason."
            },
            {
                "role": "user",
                "content": f"Classify this text: '{args.text}'"
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.0
    )

    # 3. Parse the JSON response
    result = json.loads(response.choices[0].message.content)

    # 4. Pretty print
    print(f"📝 Input:      {args.text}")
    print(f"📊 Category:   {result.get('category', 'unknown')}")
    print(f"🎯 Confidence: {result.get('confidence', 'N/A')}")
    print(f"💬 Reason:     {result.get('reason', 'N/A')}")


if __name__ == "__main__":
    main()
