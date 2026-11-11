# Program: Calculate a library fine based on overdue days
# 0 days      -> no fine
# 1-5 days    -> Rs. 2 per day
# 6-10 days   -> Rs. 5 per day
# Above 10    -> Rs. 10 per day
# (The rate for the slab is applied to ALL overdue days.)

# ---------- INPUT (used by both solutions) ----------
days = int(input("Enter number of overdue days: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if days <= 0:                        # not overdue
    fine = 0
elif days <= 5:
    fine = days * 2
elif days <= 10:
    fine = days * 5
else:                                # more than 10 days
    fine = days * 10

print("Library fine: Rs.", fine)

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def calculate_fine(overdue_days):
    # Returns the fine amount
    if overdue_days <= 0:
        return 0
    elif overdue_days <= 5:
        return overdue_days * 2
    elif overdue_days <= 10:
        return overdue_days * 5
    else:
        return overdue_days * 10

fine = calculate_fine(days)
print("Library fine: Rs.", fine)
