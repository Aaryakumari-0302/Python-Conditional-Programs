# Check whether a given number is a multiple of the sum of its digits

number = int(input("Enter a number: "))

# Add up the digits
temp = abs(number)
digit_sum = 0
while temp > 0:
    digit_sum = digit_sum + temp % 10
    temp = temp // 10

if digit_sum == 0:
    print("Digit sum is 0, so the check is not possible.")
else:
    if number % digit_sum == 0:
        print(number, "is a multiple of the sum of its digits (", digit_sum, ").")
    else:
        print(number, "is not a multiple of the sum of its digits (", digit_sum, ").")
