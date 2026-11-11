# Check whether two numbers have the same remainder when divided by 7

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a % 7 == b % 7:
    print("Both numbers have the same remainder when divided by 7.")
else:
    print("The numbers have different remainders when divided by 7.")
