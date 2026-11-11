# Check whether a three-digit number contains any repeated digits

number = int(input("Enter a three-digit number: "))

if abs(number) < 100 or abs(number) > 999:
    print("Please enter a valid three-digit number.")
else:
    n = abs(number)
    d1 = n // 100          # hundreds digit
    d2 = (n // 10) % 10    # tens digit
    d3 = n % 10            # ones digit

    if d1 == d2 or d2 == d3 or d1 == d3:
        print("The number has repeated digits.")
    else:
        print("The number has no repeated digits.")
