# Check whether a point lies inside the first quadrant
# Method 1: Normal method
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("The point lies in the first quadrant.")

# Method 2: Function method
def check_first_quadrant(x, y):
    if x > 0 and y > 0:
        print("The point lies in the first quadrant.")

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
check_first_quadrant(x, y)
