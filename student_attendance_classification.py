# Program: Classify a student's attendance
# Low (below 60%), Moderate (60-79%), High (80% and above)

# ---------- INPUT (used by both solutions) ----------
attendance = float(input("Enter attendance percentage: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if attendance < 60:
    print("Attendance: Low")
elif attendance < 80:                # 60 up to 79.99
    print("Attendance: Moderate")
else:                                # 80 and above
    print("Attendance: High")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_attendance(percent):
    # Returns the attendance category
    if percent < 60:
        return "Low"
    elif percent < 80:
        return "Moderate"
    else:
        return "High"

result = classify_attendance(attendance)
print("Attendance:", result)
