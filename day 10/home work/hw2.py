password = "pass123"
user_pass = (input("enter a password: "))
while password == user_pass:
    print("Correct password. You have successfully logged in.")
    break
else:
    print("incorrect password, try again")