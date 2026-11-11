# Program: Classify an employee's monthly overtime hours
# None (0), Low (1-10), Moderate (11-20), High (above 20)

# ---------- INPUT (used by both solutions) ----------
overtime = int(input("Enter monthly overtime hours: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if overtime <= 0:                    # 0 hours (negative is treated as none)
    print("Overtime: None")
elif overtime <= 10:                 # 1 to 10
    print("Overtime: Low")
elif overtime <= 20:                 # 11 to 20
    print("Overtime: Moderate")
else:                                # above 20
    print("Overtime: High")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_overtime(hours):
    # Returns the overtime category
    if hours <= 0:
        return "None"
    elif hours <= 10:
        return "Low"
    elif hours <= 20:
        return "Moderate"
    else:
        return "High"

result = classify_overtime(overtime)
print("Overtime:", result)
