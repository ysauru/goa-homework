# https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0









# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
def boolean_to_string(b):
    return str(b)








# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact







# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result








# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python
def sum_of_minimums(numbers):
    result = 0
    for x in numbers:
        smallest = min(x)
        result += smallest
    return result