# Check whether the sum of the digits of a three-digit number is divisible by 3
# Method 1: Normal method
number = int(input("Enter a three-digit number: "))
value = abs(number)
digit_sum = value // 100 + (value // 10) % 10 + value % 10
if 100 <= value <= 999 and digit_sum % 3 == 0:
    print("The sum of the digits is divisible by 3.")

# Method 2: Function method
def check_digit_sum(number):
    value = abs(number)
    digit_sum = value // 100 + (value // 10) % 10 + value % 10
    if 100 <= value <= 999 and digit_sum % 3 == 0:
        print("The sum of the digits is divisible by 3.")

number = int(input("Enter a three-digit number: "))
check_digit_sum(number)
