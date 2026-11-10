# Check whether a three-digit number has 5 as its middle digit
# Method 1: Normal method
number = int(input("Enter a three-digit number: "))
if 100 <= abs(number) <= 999 and (abs(number) // 10) % 10 == 5:
    print("The middle digit is 5.")

# Method 2: Function method
def check_middle_digit(number):
    if 100 <= abs(number) <= 999 and (abs(number) // 10) % 10 == 5:
        print("The middle digit is 5.")

number = int(input("Enter a three-digit number: "))
check_middle_digit(number)
