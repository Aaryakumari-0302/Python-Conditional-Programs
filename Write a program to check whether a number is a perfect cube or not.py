# Check whether a number is a perfect cube or not

number = int(input("Enter a number: "))

# Find the nearest whole-number cube root (works for negative numbers too)
root = round(abs(number) ** (1 / 3))

if root * root * root == abs(number):
    print(number, "is a perfect cube.")
else:
    print(number, "is not a perfect cube.")
