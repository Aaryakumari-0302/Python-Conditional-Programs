# Check whether the square of a number is equal to its cube

number = int(input("Enter a number: "))

square = number * number
cube = number * number * number

if square == cube:
    print("Square and cube are equal.")
else:
    print("Square and cube are not equal.")
