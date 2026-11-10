# Check whether a rectangle is a square
# Method 1: Normal method
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
if length == breadth:
    print("The rectangle is a square.")

# Method 2: Function method
def check_square(length, breadth):
    if length == breadth:
        print("The rectangle is a square.")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
check_square(length, breadth)
