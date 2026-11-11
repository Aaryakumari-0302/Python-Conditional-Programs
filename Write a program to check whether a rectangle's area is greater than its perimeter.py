# Check whether a rectangle's area is greater than its perimeter

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)

if area > perimeter:
    print("The area is greater than the perimeter.")
else:
    print("The area is not greater than the perimeter.")
