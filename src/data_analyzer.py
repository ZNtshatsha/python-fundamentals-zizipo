import sys
from typing import Dict, List

from src.utils import greet_user


def greet_user_cli(name: str) -> None:
    print(greet_user(name))


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python data_analyzer.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    greet_user_cli(username)

    # Variables
    name: str = "DataAnalyzer"
    version: int = 1
    features: List[str] = ["Variables", "Loops", "Conditionals", "Functions"]
    config: Dict[str, object] = {"theme": "dark", "autosave": True}

    print(f"Program: {name} v{version}")
    print("Features available:", features)
    print("Configuration:", config)

    # String to int casting
    string_number: str = "42"
    int_number: int = int(string_number)
    print(f"String '{string_number}' casted to int is {int_number}")

    # Loop - for
    print("\n--- For loop with enumerate ---")
    for index, feature in enumerate(features):
        print(f"{index + 1}. {feature} (id: {id(feature)})")

    # Loop - while
    print("\n--- While loop ---")
    count: int = 0
    while count < 3:
        print(f"Count is {count}")
        count += 1

    # Conditionals
    print("\n--- Conditionals ---")
    if version < 1:
        print("Beta version")
    elif version == 1:
        print("Initial release")
    else:
        print("Updated version")

    # Tuple
    data_tuple: tuple[int, int, int] = (100, 200, 300)
    print("\nTuple:", data_tuple)

    # Dictionary
    print("\n--- Dictionary Iteration ---")
    for key in config:
        print(f"{key} => {config[key]}")


if __name__ == "__main__":
    main()
