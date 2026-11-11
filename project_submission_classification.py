# Program: Classify a student's project submission
# Early   -> submitted MORE than 3 days before the deadline
# On time -> submitted within 3 days before the deadline, up to the deadline day
# Late    -> submitted after the deadline
#
# Input meaning:
#   positive number = days BEFORE the deadline  (example: 5 means 5 days early)
#   0               = submitted on the deadline day
#   negative number = days AFTER the deadline   (example: -2 means 2 days late)

# ---------- INPUT (used by both solutions) ----------
days_before = int(input("Days before deadline (use negative if late): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if days_before > 3:
    print("Submission: Early")
elif days_before >= 0:               # 0, 1, 2 or 3 days before
    print("Submission: On time")
else:                                # negative = after the deadline
    print("Submission: Late")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_submission(days):
    # Returns the submission status
    if days > 3:
        return "Early"
    elif days >= 0:
        return "On time"
    else:
        return "Late"

result = classify_submission(days_before)
print("Submission:", result)
