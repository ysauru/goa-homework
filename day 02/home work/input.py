age = input("how old are you? ")

print(f"you are {age} years old")

is_under_age = int(age) < 18
if is_under_age == True:
    print("you are under the age of 18")
else:
    print("you are over the age of 18")
