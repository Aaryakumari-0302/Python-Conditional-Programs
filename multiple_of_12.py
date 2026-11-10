# Check whether a number is a multiple of 12
# Method 1: Normal method
number = int(input("Enter a number: "))
if number % 12 == 0:
    print("The number is a multiple of 12.")

# Method 2: Function method
def check_multiple(number):
    if number % 12 == 0:
        print("The number is a multiple of 12.")

number = int(input("Enter a number: "))
check_multiple(number)
