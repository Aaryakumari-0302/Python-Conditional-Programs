# Check whether a three-digit number contains at least one zero digit
# Method 1: Normal method
number = int(input("Enter a three-digit number: "))
value = abs(number)
if 100 <= value <= 999 and (value // 100 == 0 or (value // 10) % 10 == 0 or value % 10 == 0):
    print("The number contains at least one zero digit.")

# Method 2: Function method
def check_zero_digit(number):
    value = abs(number)
    if 100 <= value <= 999 and (value // 100 == 0 or (value // 10) % 10 == 0 or value % 10 == 0):
        print("The number contains at least one zero digit.")

number = int(input("Enter a three-digit number: "))
check_zero_digit(number)
