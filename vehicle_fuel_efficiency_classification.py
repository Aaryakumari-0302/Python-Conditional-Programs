# Program: Classify a vehicle's fuel efficiency
# Poor (below 10 km/L), Average (10-15 km/L),
# Good (above 15 up to 20 km/L), Excellent (above 20 km/L)

# ---------- INPUT (used by both solutions) ----------
mileage = float(input("Enter fuel efficiency (km/L): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if mileage < 10:
    print("Fuel efficiency: Poor")
elif mileage <= 15:                  # 10 to 15
    print("Fuel efficiency: Average")
elif mileage <= 20:                  # above 15 up to 20
    print("Fuel efficiency: Good")
else:                                # above 20
    print("Fuel efficiency: Excellent")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_fuel_efficiency(kmpl):
    # Returns the fuel efficiency category
    if kmpl < 10:
        return "Poor"
    elif kmpl <= 15:
        return "Average"
    elif kmpl <= 20:
        return "Good"
    else:
        return "Excellent"

result = classify_fuel_efficiency(mileage)
print("Fuel efficiency:", result)
