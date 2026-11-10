# Check whether the sum of three numbers is greater than 150
# Method 1: Normal method
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))
if first + second + third > 150:
    print("The sum is greater than 150.")

# Method 2: Function method
def check_sum(first, second, third):
    if first + second + third > 150:
        print("The sum is greater than 150.")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))
check_sum(first, second, third)
