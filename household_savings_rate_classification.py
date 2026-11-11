# Program: Classify a monthly household savings rate
# Poor (below 5%), Fair (5-15%), Good (above 15 up to 30%), Excellent (above 30%)

# ---------- INPUT (used by both solutions) ----------
savings_rate = float(input("Enter monthly savings rate (%): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if savings_rate < 5:
    print("Savings rate: Poor")
elif savings_rate <= 15:             # 5 to 15
    print("Savings rate: Fair")
elif savings_rate <= 30:             # above 15 up to 30
    print("Savings rate: Good")
else:                                # above 30
    print("Savings rate: Excellent")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_savings(rate):
    # Returns the savings category
    if rate < 5:
        return "Poor"
    elif rate <= 15:
        return "Fair"
    elif rate <= 30:
        return "Good"
    else:
        return "Excellent"

result = classify_savings(savings_rate)
print("Savings rate:", result)
