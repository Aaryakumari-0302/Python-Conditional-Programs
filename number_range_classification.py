# Program: Classify a number as less than 25, between 25 and 75, or greater than 75

# ---------- INPUT (used by both solutions) ----------
number = float(input("Enter a number: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if number < 25:
    print(number, "is less than 25")
elif number <= 75:                   # 25 to 75 (both included)
    print(number, "is between 25 and 75")
else:                                # more than 75
    print(number, "is greater than 75")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_range(num):
    # Returns which range the number belongs to
    if num < 25:
        return "Less than 25"
    elif num <= 75:
        return "Between 25 and 75"
    else:
        return "Greater than 75"

result = classify_range(number)
print(number, "->", result)
