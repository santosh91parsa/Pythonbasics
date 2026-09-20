"""
Example 2: Connecting argparse to a Class and Method
Run with:
    python examples/02_class_and_method.py Arabica --sugar 2
    python examples/02_class_and_method.py Robusta
"""
import argparse

# 1. Blueprint (Class)
class CoffeeMaker:
    def __init__(self, beans: str, sugar: int = 1):
        self.beans = beans
        self.sugar = sugar

    # Action (Method)
    def brew(self):
        print(f"[CoffeeMaker] Brewing fresh {self.beans} coffee with {self.sugar} spoon(s) of sugar!")


def main():
    # 2. Setup parser
    parser = argparse.ArgumentParser(description="Brew coffee with custom options")
    parser.add_argument("beans", help="Type of coffee beans (e.g. Arabica, Robusta)")
    parser.add_argument("--sugar", type=int, default=1, help="Spoons of sugar (default: 1)")

    # 3. Parse arguments into args object
    args = parser.parse_args()

    # 4. Initialize the Class (Object created from Blueprint)
    machine = CoffeeMaker(beans=args.beans, sugar=args.sugar)

    # 5. Call the Method on the Object
    machine.brew()


if __name__ == "__main__":
    main()
