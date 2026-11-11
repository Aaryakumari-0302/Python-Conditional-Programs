# Program: Calculate a taxi fare based on distance
# Up to 2 km          -> Rs. 50 (fixed)
# 2 km to 10 km       -> Rs. 50 + Rs. 15 for each extra km after 2 km
# Beyond 10 km        -> Rs. 50 + (8 km x Rs. 15) + Rs. 12 for each km after 10 km
#                        (8 km x 15 = 120, so base is 50 + 120 = 170)

# ---------- INPUT (used by both solutions) ----------
distance = float(input("Enter distance travelled (km): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if distance <= 2:
    fare = 50
elif distance <= 10:
    extra_km = distance - 2          # km after the first 2 km
    fare = 50 + extra_km * 15
else:
    extra_km = distance - 10         # km after the first 10 km
    fare = 170 + extra_km * 12       # 170 = fare for exactly 10 km

print("Taxi fare: Rs.", fare)

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def calculate_fare(km):
    # Returns the taxi fare for the given distance
    if km <= 2:
        return 50
    elif km <= 10:
        return 50 + (km - 2) * 15
    else:
        return 170 + (km - 10) * 12

fare = calculate_fare(distance)
print("Taxi fare: Rs.", fare)
