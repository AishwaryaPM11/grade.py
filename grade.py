mark = int(input("Enter student's mark: "))


if mark >= 90:
    grade = 'A'
elif mark >= 80:
    grade = 'B'
elif mark >= 70:
    grade = 'C'
elif mark >= 60:
    grade = 'D'
else:
    grade = 'Fail'
print(f"Grade: {grade}")
def get_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'Fail'

if _name_ == "_main_":
    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for student {i}: "))
        marks.append(mark)

    average = compute_average(marks)
    grade = get_grade(average)

    print(f"\nAverage Marks: {average:.2f}")
    print(f"Grade: {grade}")