# Program: Determine a student's certification level based on a practical score
# Beginner (below 40), Intermediate (40-59), Proficient (60-79), Expert (80 and above)

# ---------- INPUT (used by both solutions) ----------
score = float(input("Enter practical score: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if score < 40:
    print("Certification level: Beginner")
elif score < 60:                     # 40 up to 59.99
    print("Certification level: Intermediate")
elif score < 80:                     # 60 up to 79.99
    print("Certification level: Proficient")
else:                                # 80 and above
    print("Certification level: Expert")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def certification_level(s):
    # Returns the certification level
    if s < 40:
        return "Beginner"
    elif s < 60:
        return "Intermediate"
    elif s < 80:
        return "Proficient"
    else:
        return "Expert"

result = certification_level(score)
print("Certification level:", result)
