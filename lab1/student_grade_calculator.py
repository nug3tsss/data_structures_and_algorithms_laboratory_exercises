students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [
    [85, 92, 78, 94],
    [76, 83, 91, 87],
    [94, 89, 96, 93],
    [67, 74, 82, 79],
    [88, 85, 90, 92]
]

def calculate_average(scores):
    total_score = 0

    for score in scores:
        total_score += score
    
    return total_score / len(scores)

def get_letter_average(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print("=== STUDENT GRADE REPORT ===")

for i in range(len(students)):
    student = students[i]
    student_scores = scores[i]

    student_average = calculate_average(student_scores)
    student_letter_grade = get_letter_average(student_average)

    print(f"{student+":":<10} Average: {student_average:.2f}, Grade: {student_letter_grade}")

    