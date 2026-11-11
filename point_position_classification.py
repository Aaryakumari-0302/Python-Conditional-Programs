# Program: Classify a point as lying at the origin, on the x-axis, on the y-axis,
# or in one of the four quadrants

# ---------- INPUT (used by both solutions) ----------
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if x == 0 and y == 0:
    print("The point is at the Origin")
elif y == 0:                         # x is not 0, y is 0
    print("The point lies on the X-axis")
elif x == 0:                         # y is not 0, x is 0
    print("The point lies on the Y-axis")
elif x > 0 and y > 0:
    print("The point is in Quadrant 1")
elif x < 0 and y > 0:
    print("The point is in Quadrant 2")
elif x < 0 and y < 0:
    print("The point is in Quadrant 3")
else:                                # x > 0 and y < 0
    print("The point is in Quadrant 4")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_point(px, py):
    # Returns the position of the point
    if px == 0 and py == 0:
        return "Origin"
    elif py == 0:
        return "On the X-axis"
    elif px == 0:
        return "On the Y-axis"
    elif px > 0 and py > 0:
        return "Quadrant 1"
    elif px < 0 and py > 0:
        return "Quadrant 2"
    elif px < 0 and py < 0:
        return "Quadrant 3"
    else:
        return "Quadrant 4"

result = classify_point(x, y)
print("Point position:", result)
