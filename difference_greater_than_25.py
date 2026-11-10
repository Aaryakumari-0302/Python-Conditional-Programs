# Check whether the difference between two numbers is greater than 25
# Method 1: Normal method
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
if abs(first - second) > 25:
    print("The difference is greater than 25.")

# Method 2: Function method
def check_difference(first, second):
    if abs(first - second) > 25:
        print("The difference is greater than 25.")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
check_difference(first, second)
