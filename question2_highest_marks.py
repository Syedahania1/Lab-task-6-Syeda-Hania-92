marks = {
    "Ali": 85,
    "Sara": 95,
    "Ahmed": 95,
    "Noor": 78
}

highest_marks = max(marks.values())

for student, score in marks.items():
    if score == highest_marks:
        print(student, ":", score)
