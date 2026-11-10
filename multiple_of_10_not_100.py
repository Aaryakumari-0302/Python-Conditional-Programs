# Check whether a number is a multiple of 10 but not a multiple of 100
# Method 1: Normal method
number = int(input("Enter a number: "))
if number % 10 == 0 and number % 100 != 0:
    print("The number is a multiple of 10 but not of 100.")

# Method 2: Function method
def check_multiple(number):
    if number % 10 == 0 and number % 100 != 0:
        print("The number is a multiple of 10 but not of 100.")

number = int(input("Enter a number: "))
check_multiple(number)
