# Check whether the square of a number is greater than 500
# Method 1: Normal method
number = float(input("Enter a number: "))
if number ** 2 > 500:
    print("The square is greater than 500.")

# Method 2: Function method
def check_square(number):
    if number ** 2 > 500:
        print("The square is greater than 500.")

number = float(input("Enter a number: "))
check_square(number)
