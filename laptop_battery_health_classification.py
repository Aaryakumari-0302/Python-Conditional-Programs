# Program: Classify a laptop's battery health
# Excellent (90% and above), Good (70-89%), Fair (50-69%), Poor (below 50%)

# ---------- INPUT (used by both solutions) ----------
health = float(input("Enter battery health (%): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if health >= 90:
    print("Battery health: Excellent")
elif health >= 70:                   # 70 up to 89.99
    print("Battery health: Good")
elif health >= 50:                   # 50 up to 69.99
    print("Battery health: Fair")
else:                                # below 50
    print("Battery health: Poor")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_battery_health(percent):
    # Returns the battery health category
    if percent >= 90:
        return "Excellent"
    elif percent >= 70:
        return "Good"
    elif percent >= 50:
        return "Fair"
    else:
        return "Poor"

result = classify_battery_health(health)
print("Battery health:", result)
