"""
Example 1: Basic argparse usage
Run with:
    python examples/01_simple_argparse.py Bob
    python examples/01_simple_argparse.py Bob --sugar 3
    python examples/01_simple_argparse.py --help
"""
import argparse

def main():
    # 1. Create the parser (Object from Class)
    parser = argparse.ArgumentParser(description="Simple Coffee Order CLI")

    # 2. Add arguments
    parser.add_argument("name", help="Name of customer")
    parser.add_argument("--sugar", type=int, default=1, help="Spoons of sugar (default: 1)")
    parser.add_argument("--iced", action="store_true", help="Make it iced coffee")

    # 3. Parse arguments
    args = parser.parse_args()

    # 4. Use the results
    drink_type = "Iced Coffee" if args.iced else "Hot Coffee"
    print(f"Preparing {drink_type} for {args.name} with {args.sugar} spoon(s) of sugar!")

if __name__ == "__main__":
    main()
