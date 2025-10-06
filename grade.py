mark1 = int(input("Enter student's mark: "))
mark2 = int(input("Enter student's mark: "))
mark3= int(input("Enter student's mark: "))
mark4= int(input("Enter student's mark: "))
mark5= int(input("Enter student's mark: "))
average=(mark1+mark2+mark3+mark4+mark5)/5




if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'Fail'
print(f"Grade: {grade}")
