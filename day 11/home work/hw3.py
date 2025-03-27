num = 3
user_input = 0

while user_input != num:
    user_input = int(input("please enter the number: "))

    if user_input == num:
        print("You won")
    else:
        print("try again")