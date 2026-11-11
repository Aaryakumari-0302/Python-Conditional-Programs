# Program: Determine a student's academic standing based on GPA
# Excellent (3.7-4.0), Good (3.0 to below 3.7),
# Satisfactory (2.0 to below 3.0), Academic Warning (below 2.0)

# ---------- INPUT (used by both solutions) ----------
gpa = float(input("Enter GPA (0.0 to 4.0): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if gpa >= 3.7:
    print("Academic standing: Excellent")
elif gpa >= 3.0:                     # 3.0 up to below 3.7
    print("Academic standing: Good")
elif gpa >= 2.0:                     # 2.0 up to below 3.0
    print("Academic standing: Satisfactory")
else:                                # below 2.0
    print("Academic standing: Academic Warning")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def academic_standing(g):
    # Returns the academic standing
    if g >= 3.7:
        return "Excellent"
    elif g >= 3.0:
        return "Good"
    elif g >= 2.0:
        return "Satisfactory"
    else:
        return "Academic Warning"

result = academic_standing(gpa)
print("Academic standing:", result)
