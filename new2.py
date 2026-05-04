
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"


username_input = input("Enter username: ")
password_input = input("Enter password: ")

if username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD:
    print("Access granted! Welcome, " + username_input + ".")
else:
    print("Access denied! Incorrect username or password.")
if username_input == CORRECT_USERNAME:
    print("correct name")
else:
    print("wrong name ") 

if username_input == CORRECT_PASSWORD:
    print("correct password")
else:
    print("wrong password ") 


