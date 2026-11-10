# Check whether a number is divisible by 9
# Method 1: Normal method
number = int(input("Enter a number: "))
if number % 9 == 0:
    print("The number is divisible by 9.")

# Method 2: Function method
def check_divisible_by_9(number):
    if number % 9 == 0:
        print("The number is divisible by 9.")

number = int(input("Enter a number: "))
check_divisible_by_9(number)
