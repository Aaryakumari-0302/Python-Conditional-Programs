# Check whether a four-digit number has the same first and last digits
# Method 1: Normal method
number = int(input("Enter a four-digit number: "))
value = abs(number)
if 1000 <= value <= 9999 and value // 1000 == value % 10:
    print("The first and last digits are the same.")

# Method 2: Function method
def check_first_last_digit(number):
    value = abs(number)
    if 1000 <= value <= 9999 and value // 1000 == value % 10:
        print("The first and last digits are the same.")

number = int(input("Enter a four-digit number: "))
check_first_last_digit(number)
