# Check whether a number is a Harshad number
# A Harshad number is divisible by the sum of its digits.
# Method 1: Normal method
number = int(input("Enter a positive number: "))
value = abs(number)
digit_sum = sum(int(digit) for digit in str(value))
if value > 0 and value % digit_sum == 0:
    print("It is a Harshad number.")

# Method 2: Function method
def check_harshad(number):
    value = abs(number)
    digit_sum = sum(int(digit) for digit in str(value))
    if value > 0 and value % digit_sum == 0:
        print("It is a Harshad number.")

number = int(input("Enter a positive number: "))
check_harshad(number)
