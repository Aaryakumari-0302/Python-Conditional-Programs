# Check whether a number is divisible by 4 but not by 6
# Method 1: Normal method
number = int(input("Enter a number: "))
if number % 4 == 0 and number % 6 != 0:
    print("The number is divisible by 4 but not by 6.")

# Method 2: Function method
def check_number(number):
    if number % 4 == 0 and number % 6 != 0:
        print("The number is divisible by 4 but not by 6.")

number = int(input("Enter a number: "))
check_number(number)
