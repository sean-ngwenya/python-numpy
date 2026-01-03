"""
Simulate exam scores for 5 classes (rows) with 30 students each:
    Find top 5% performers per class
"""

import numpy as np


def simulate_exam_scores(classes=5, students_per_class=30):
    """Simulate exam scores for a given number of classes and students."""
    return np.random.randint(0, 101, size=(classes, students_per_class))


def find_top_performers(scores, percentile=95):
    """Find students who scored above the given percentile in each class."""
    top_performers = []
    for class_scores in scores:
        threshold = np.percentile(class_scores, percentile)
        top_students = class_scores[class_scores >= threshold]
        top_performers.append(top_students)
    return top_performers


def find_to_performers(scores, percentile=95):
    """Find students who scored above the given percentile in each class."""
    thresholds = np.percentile(scores, percentile, axis=1)
    top_performers = []
    for i, class_scores in enumerate(scores):
        top_students = class_scores[class_scores >= thresholds[i]]
        top_performers.append(top_students)
    return top_performers


if __name__ == "__main__":
    exam_scores = simulate_exam_scores()
    top_performers = find_to_performers(exam_scores)

    for i, performers in enumerate(top_performers):
        print(f"Class {i + 1} top performers (above 95th percentile): {performers}")
