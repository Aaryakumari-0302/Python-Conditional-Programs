# Program: Classify a delivery order based on distance
# Local (up to 5 km), Nearby (above 5 and up to 15 km), Distant (above 15 km)

# ---------- INPUT (used by both solutions) ----------
distance = float(input("Enter delivery distance (km): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if distance <= 5:
    print("Delivery type: Local")
elif distance <= 15:                 # above 5 and up to 15
    print("Delivery type: Nearby")
else:                                # above 15
    print("Delivery type: Distant")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_delivery(km):
    # Returns the delivery type
    if km <= 5:
        return "Local"
    elif km <= 15:
        return "Nearby"
    else:
        return "Distant"

result = classify_delivery(distance)
print("Delivery type:", result)
