# Check whether a person's name has more than 10 characters
# Method 1: Normal method
name = input("Enter your name: ")
if len(name) > 10:
    print("The name has more than 10 characters.")

# Method 2: Function method
def check_name_length(name):
    if len(name) > 10:
        print("The name has more than 10 characters.")

name = input("Enter your name: ")
check_name_length(name)
