# Program: Calculate a water bill using slab rates
# First 1000 litres        -> Rs. 0.02 per litre
# Next 1000 litres         -> Rs. 0.03 per litre
# Any litres above 2000    -> Rs. 0.05 per litre
# (Each slab is charged only for the litres that fall inside it.)

# ---------- INPUT (used by both solutions) ----------
litres = float(input("Enter water used (litres): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if litres <= 1000:
    bill = litres * 0.02
elif litres <= 2000:
    bill = 1000 * 0.02 + (litres - 1000) * 0.03
else:                                # more than 2000 litres
    bill = 1000 * 0.02 + 1000 * 0.03 + (litres - 2000) * 0.05

print("Water bill: Rs.", round(bill, 2))

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def calculate_water_bill(l):
    # Returns the water bill amount
    if l <= 1000:
        return l * 0.02
    elif l <= 2000:
        return 1000 * 0.02 + (l - 1000) * 0.03
    else:
        return 1000 * 0.02 + 1000 * 0.03 + (l - 2000) * 0.05

bill = calculate_water_bill(litres)
print("Water bill: Rs.", round(bill, 2))
