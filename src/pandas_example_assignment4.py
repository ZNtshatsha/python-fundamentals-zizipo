import pandas as pd

# Example DataFrame
data: dict[str, list[str | int]] = {
    "Name": ["God", "Zodwa", "James"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 95],
}

df: pd.DataFrame = pd.DataFrame(data)


def get_average_score(df: pd.DataFrame) -> float:
    """Return the average score from the DataFrame."""
    score_mean: float = float(df["Score"].mean())
    return score_mean


def add_new_student(df: pd.DataFrame, name: str, age: int, score: int) -> pd.DataFrame:
    """Add a new student to the DataFrame and return the updated one."""
    new_row = pd.DataFrame({"Name": [name], "Age": [age], "Score": [score]})
    updated_df: pd.DataFrame = pd.concat([df, new_row], ignore_index=True)
    return updated_df


def top_student(df: pd.DataFrame) -> str:
    """Return the name of the student with the highest score."""
    top_name: str = str(df.loc[df["Score"].idxmax(), "Name"])
    return top_name


if __name__ == "__main__":
    avg_score: float = get_average_score(df)
    df = add_new_student(df, "David", 28, 88)
    top: str = top_student(df)

    print(f"Average Score: {avg_score}")
    print(f"Top student: {top}")
