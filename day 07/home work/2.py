grade = float(input("Enter your grade: "))


if round(grade) >= 90:
    print("your grade is A")
elif round(grade) >= 70:
    print("your grade is B")
elif round(grade) >= 50:
    print("your grade is C")
else:
    print("your grade is F")
