# Program: Classify a transaction risk level using the transaction amount
# and the number of failed login attempts.
# The question says "define clear thresholds", so these are the thresholds used.
# You can change the numbers to any values you like.
#
# Suspicious : amount above Rs. 100000  OR  5 or more failed attempts
# High       : amount above Rs. 50000   OR  3 or more failed attempts
# Medium     : amount above Rs. 10000   OR  1 or more failed attempts
# Low        : everything else
#
# The checks go from the most serious level to the least serious level.

# ---------- INPUT (used by both solutions) ----------
amount = float(input("Enter transaction amount (Rs.): "))
failed_attempts = int(input("Enter number of failed login attempts: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if amount > 100000 or failed_attempts >= 5:
    print("Risk level: Suspicious")
elif amount > 50000 or failed_attempts >= 3:
    print("Risk level: High")
elif amount > 10000 or failed_attempts >= 1:
    print("Risk level: Medium")
else:
    print("Risk level: Low")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_risk(money, attempts):
    # Returns the risk level of the transaction
    if money > 100000 or attempts >= 5:
        return "Suspicious"
    elif money > 50000 or attempts >= 3:
        return "High"
    elif money > 10000 or attempts >= 1:
        return "Medium"
    else:
        return "Low"

result = classify_risk(amount, failed_attempts)
print("Risk level:", result)
