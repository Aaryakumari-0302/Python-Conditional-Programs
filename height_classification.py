# Program: Classify a person's height
# Short (below 150 cm), Average (150-175 cm), Tall (above 175 cm)

# ---------- INPUT (used by both solutions) ----------
height = float(input("Enter height in cm: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if height < 150:
    print("Height category: Short")
elif height <= 175:                  # 150 to 175 (both included)
    print("Height category: Average")
else:                                # above 175
    print("Height category: Tall")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_height(h):
    # Returns the height category
    if h < 150:
        return "Short"
    elif h <= 175:
        return "Average"
    else:
        return "Tall"

result = classify_height(height)
print("Height category:", result)
