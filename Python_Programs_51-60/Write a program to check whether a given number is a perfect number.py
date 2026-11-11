# Check whether a number is a perfect number
# A perfect number equals the sum of its proper divisors (e.g. 6 = 1 + 2 + 3)

number = int(input("Enter a number: "))

if number > 0:
    divisor_sum = 0

    for i in range(1, number):
        if number % i == 0:
            divisor_sum = divisor_sum + i

    if divisor_sum == number:
        print(number, "is a perfect number.")
    else:
        print(number, "is NOT a perfect number.")
else:
    print("Please enter a positive number.")
