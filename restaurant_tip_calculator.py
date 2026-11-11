# Program: Calculate a restaurant tip percentage based on service rating
# 5 stars = 20%, 4 stars = 15%, 3 stars = 10%, otherwise = 0%

# ---------- INPUT (used by both solutions) ----------
stars = int(input("Enter service rating (stars): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if stars == 5:
    tip = 20
elif stars == 4:
    tip = 15
elif stars == 3:
    tip = 10
else:                                # 1, 2 stars or anything else
    tip = 0

print("Tip percentage:", tip, "%")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def calculate_tip(rating):
    # Returns the tip percentage
    if rating == 5:
        return 20
    elif rating == 4:
        return 15
    elif rating == 3:
        return 10
    else:
        return 0

tip = calculate_tip(stars)
print("Tip percentage:", tip, "%")
