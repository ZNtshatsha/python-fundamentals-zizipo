# Only import what is actually used!

<<<<<<< HEAD
from src.utils import some_function  # or correct name if not `some_function`
=======
>>>>>>> bfa5463 (Added new assignment files and updates)

# If you still use pandas or pydantic, keep these; otherwise remove them
# import pandas as pd
# from pydantic import BaseModel

# Add other imports **here at the top**, not inside functions

import sys

<<<<<<< HEAD
from src.utils import some_function  # adjust to your function name
=======

>>>>>>> bfa5463 (Added new assignment files and updates)
def greet_user(name: str) -> None:
    print(f"Hello,{name}")  # Use the utils function here

def main() -> None:
    # Command-line argument handling
    if len(sys.argv) < 2:
        print("Usage: python data_analyzer.py <username>")
        sys.exit(1)

    username = sys.argv[1]
    greet_user(username)  # call greet_user here

    # Variables
    name = "DataAnalyzer"
    version = 1
    features = ["Variables", "Loops", "Conditionals", "Functions"]
    config = {"theme": "dark", "autosave": True}

    print(f"Program: {name} v{version}")
    print("Features available:", features)
    print("Configuration:", config)

    # String to int casting
    string_number = "42"
    int_number = int(string_number)
    print(f"String '{string_number}' casted to int is {int_number}")

    # Loop - for
    print("\n--- For loop with enumerate ---")
    for index, feature in enumerate(features):
        print(f"{index + 1}. {feature} (id: {id(feature)})")

    # Loop - while
    print("\n--- While loop ---")
    count = 0
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
    data_tuple = (100, 200, 300)
    print("\nTuple:", data_tuple)

    # Dictionary
    print("\n--- Dictionary Iteration ---")
    for key in config:
        print(f"{key} => {config[key]}")

if __name__ == "__main__":
    main()
