numbers = []
for i in range(10):
    num = int(input("enter a number: "))
    numbers.append(num)
for num in numbers:
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")