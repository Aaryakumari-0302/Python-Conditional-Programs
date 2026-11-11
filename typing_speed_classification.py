# Program: Classify a student's typing speed
# Beginner (below 20 WPM), Intermediate (20-40 WPM), Advanced (above 40 WPM)

# ---------- INPUT (used by both solutions) ----------
wpm = float(input("Enter typing speed (WPM): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if wpm < 20:
    print("Typing level: Beginner")
elif wpm <= 40:                      # 20 to 40 (both included)
    print("Typing level: Intermediate")
else:                                # above 40
    print("Typing level: Advanced")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_typing_speed(speed):
    # Returns the typing level
    if speed < 20:
        return "Beginner"
    elif speed <= 40:
        return "Intermediate"
    else:
        return "Advanced"

result = classify_typing_speed(wpm)
print("Typing level:", result)
