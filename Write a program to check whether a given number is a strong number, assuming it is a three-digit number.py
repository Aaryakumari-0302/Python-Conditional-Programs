# Check whether a given three-digit number is a strong number
# (Strong number: sum of factorials of its digits equals the number. Example: 145)

number = int(input("Enter a three-digit number: "))

if number < 100 or number > 999:
    print("Please enter a valid three-digit number.")
else:
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10

        # Find factorial of the digit
        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        temp = temp // 10

    if total == number:
        print(number, "is a strong number.")
    else:
        print(number, "is not a strong number.")
