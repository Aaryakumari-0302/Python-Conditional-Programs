# Program: Classify a person's daily screen time
# Low (below 2 hours), Moderate (2-5 hours), High (above 5 hours)

# ---------- INPUT (used by both solutions) ----------
hours = float(input("Enter daily screen time (hours): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if hours < 2:
    print("Screen time: Low")
elif hours <= 5:                     # 2 to 5 (both included)
    print("Screen time: Moderate")
else:                                # above 5
    print("Screen time: High")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_screen_time(h):
    # Returns the screen time category
    if h < 2:
        return "Low"
    elif h <= 5:
        return "Moderate"
    else:
        return "High"

result = classify_screen_time(hours)
print("Screen time:", result)
