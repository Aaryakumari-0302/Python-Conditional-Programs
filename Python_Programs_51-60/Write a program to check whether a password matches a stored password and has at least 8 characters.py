# Check whether a password matches the stored password and has at least 8 characters

stored_password = "Secret123"

entered_password = input("Enter your password: ")

if entered_password == stored_password and len(entered_password) >= 8:
    print("Password is correct and valid.")
else:
    print("Password is incorrect or has fewer than 8 characters.")
