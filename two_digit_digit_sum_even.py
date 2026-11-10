# Check whether the sum of the digits of a two-digit number is even
# Method 1: Normal method
number = int(input("Enter a two-digit number: "))
if 10 <= abs(number) <= 99 and ((abs(number) // 10) + (abs(number) % 10)) % 2 == 0:
    print("The sum of the digits is even.")

# Method 2: Function method
def check_digit_sum(number):
    if 10 <= abs(number) <= 99 and ((abs(number) // 10) + (abs(number) % 10)) % 2 == 0:
        print("The sum of the digits is even.")

number = int(input("Enter a two-digit number: "))
check_digit_sum(number)
