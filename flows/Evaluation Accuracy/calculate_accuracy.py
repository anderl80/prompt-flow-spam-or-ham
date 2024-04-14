from typing import List

from promptflow import tool, log_metric


@tool
def calculate_accuracy(grades: List[str]):
    # calculate accuracy
    accuracy = round((grades.count("Correct") / len(grades)), 2)
    log_metric("accuracy", accuracy)

    return accuracy
