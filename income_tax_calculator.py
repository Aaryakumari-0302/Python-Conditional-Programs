# Program: Calculate income tax using simplified annual income bands
# Up to Rs. 3 lakh              -> 0%
# Above 3 lakh up to 6 lakh     -> 5%
# Above 6 lakh up to 10 lakh    -> 10%
# Above 10 lakh                 -> 20%
# The selected rate is applied to the ENTIRE income.
# (1 lakh = 100000)

# ---------- INPUT (used by both solutions) ----------
income = float(input("Enter annual income (Rs.): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if income <= 300000:
    rate = 0
elif income <= 600000:
    rate = 5
elif income <= 1000000:
    rate = 10
else:                                # above 10 lakh
    rate = 20

tax = income * rate / 100            # percentage of the whole income
print("Tax rate:", rate, "%")
print("Income tax: Rs.", tax)

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def get_tax_rate(annual_income):
    # Returns the tax rate (in percent) for the income
    if annual_income <= 300000:
        return 0
    elif annual_income <= 600000:
        return 5
    elif annual_income <= 1000000:
        return 10
    else:
        return 20

def calculate_tax(annual_income):
    # Returns the tax amount
    rate = get_tax_rate(annual_income)
    return annual_income * rate / 100

rate = get_tax_rate(income)
tax = calculate_tax(income)
print("Tax rate:", rate, "%")
print("Income tax: Rs.", tax)
