username = input("Enter username: ")
password = input("Enter password: ")
valid = False
for char in username:
    if char.isalnum():
        valid = True
    else:
        valid = False
        break
if valid:
    print("Username is valid")
else:
    print("Invalid username")