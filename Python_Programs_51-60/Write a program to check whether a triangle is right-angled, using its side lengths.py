# Check whether a triangle is right-angled using its side lengths
# Pythagoras: the square of the longest side equals the sum of squares of the other two

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a > 0 and b > 0 and c > 0:
    # Try each side as the longest side (hypotenuse)
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("The triangle is right-angled.")
    else:
        print("The triangle is NOT right-angled.")
else:
    print("Side lengths must be positive.")
