# Check whether three angles form a valid triangle and whether their sum is exactly 180

a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

total = a + b + c

# Check the sum
if total == 180:
    print("The sum of the angles is exactly 180 degrees.")
else:
    print("The sum of the angles is", total, "- it is NOT 180 degrees.")

# A valid triangle needs every angle above 0 and a sum of exactly 180
if a > 0 and b > 0 and c > 0 and total == 180:
    print("These angles can form a valid triangle.")
else:
    print("These angles cannot form a valid triangle.")
