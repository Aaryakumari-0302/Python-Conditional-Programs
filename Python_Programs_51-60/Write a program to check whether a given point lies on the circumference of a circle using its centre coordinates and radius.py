# Check whether a point lies on the circumference of a circle
# Formula: (x - h)^2 + (y - k)^2 = r^2, where (h, k) is the centre

h = float(input("Enter centre x-coordinate: "))
k = float(input("Enter centre y-coordinate: "))
r = float(input("Enter radius: "))
x = float(input("Enter point x-coordinate: "))
y = float(input("Enter point y-coordinate: "))

if r > 0:
    left_side = (x - h) ** 2 + (y - k) ** 2
    right_side = r ** 2

    # A tiny tolerance handles decimal rounding errors
    if abs(left_side - right_side) < 0.000001:
        print("The point lies on the circumference of the circle.")
    else:
        print("The point does NOT lie on the circumference of the circle.")
else:
    print("Radius must be positive.")
