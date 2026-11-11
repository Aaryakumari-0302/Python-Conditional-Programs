# Check whether a four-digit number is divisible by the sum of its first and last digits

number = int(input("Enter a four-digit number: "))

if number >= 1000 and number <= 9999:
    first_digit = number // 1000
    last_digit = number % 10
    digit_sum = first_digit + last_digit

    if number % digit_sum == 0:
        print(number, "is divisible by", digit_sum, "(sum of first and last digits).")
    else:
        print(number, "is NOT divisible by", digit_sum, "(sum of first and last digits).")
else:
    print("Please enter a valid four-digit number.")
