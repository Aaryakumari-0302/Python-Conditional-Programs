# Program: Classify a product's rating
# Poor (1-2), Average (3), Excellent (4-5)

# ---------- INPUT (used by both solutions) ----------
rating = int(input("Enter product rating (1 to 5): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if rating == 1 or rating == 2:
    print("Rating category: Poor")
elif rating == 3:
    print("Rating category: Average")
elif rating == 4 or rating == 5:
    print("Rating category: Excellent")
else:                                # anything outside 1 to 5
    print("Invalid rating! Enter a value from 1 to 5.")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_rating(r):
    # Returns the rating category
    if r == 1 or r == 2:
        return "Poor"
    elif r == 3:
        return "Average"
    elif r == 4 or r == 5:
        return "Excellent"
    else:
        return "Invalid rating"

result = classify_rating(rating)
print("Rating category:", result)
