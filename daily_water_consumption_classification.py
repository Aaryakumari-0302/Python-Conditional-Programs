# Program: Classify a person's daily water consumption
# Low (below 1 litre), Moderate (1-2 litres), High (above 2 litres)

# ---------- INPUT (used by both solutions) ----------
litres = float(input("Enter daily water consumption (litres): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if litres < 1:
    print("Water consumption: Low")
elif litres <= 2:                    # 1 to 2 (both included)
    print("Water consumption: Moderate")
else:                                # above 2
    print("Water consumption: High")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_water(l):
    # Returns the water consumption category
    if l < 1:
        return "Low"
    elif l <= 2:
        return "Moderate"
    else:
        return "High"

result = classify_water(litres)
print("Water consumption:", result)
