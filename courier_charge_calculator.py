# Program: Calculate a courier charge based on parcel weight
# The question does not give the prices, so these SAMPLE charges are used.
# You can change the numbers below to any prices you like.
#
# Up to 1 kg               -> Rs. 50
# Above 1 kg up to 5 kg    -> Rs. 100
# Above 5 kg up to 10 kg   -> Rs. 180
# Above 10 kg              -> Rs. 250

# ---------- INPUT (used by both solutions) ----------
weight = float(input("Enter parcel weight (kg): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if weight <= 1:
    charge = 50
elif weight <= 5:
    charge = 100
elif weight <= 10:
    charge = 180
else:                                # above 10 kg
    charge = 250

print("Courier charge: Rs.", charge)

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def calculate_courier_charge(kg):
    # Returns the courier charge for the parcel weight
    if kg <= 1:
        return 50
    elif kg <= 5:
        return 100
    elif kg <= 10:
        return 180
    else:
        return 250

charge = calculate_courier_charge(weight)
print("Courier charge: Rs.", charge)
