operator = (input("Please enter a operator (+, -, *, /,< , >, <=, >=): "))
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
elif operator == "<":
    result = num1 < num2
    print(result)
elif operator == ">":
    result = num1 > num2
    print(num1 > num2)
elif operator == ">=":
    result = num1 >= num2
    print(num1 >= num2)
elif operator == "<=":
    result = num1 <= num2
    print(num1 <= num2)
