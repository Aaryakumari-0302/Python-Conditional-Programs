# Check whether a number ends with the digit 3
# Method 1: Normal method
number = int(input("Enter a number: "))
if abs(number) % 10 == 3:
    print("The number ends with 3.")

# Method 2: Function method
def check_last_digit(number):
    if abs(number) % 10 == 3:
        print("The number ends with 3.")

number = int(input("Enter a number: "))
check_last_digit(number)
