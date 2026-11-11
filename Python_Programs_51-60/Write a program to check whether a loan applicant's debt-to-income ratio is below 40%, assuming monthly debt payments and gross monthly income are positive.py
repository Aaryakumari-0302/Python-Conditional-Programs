# Check whether the debt-to-income (DTI) ratio is below 40%
# Both values are assumed to be positive

monthly_debt = float(input("Enter monthly debt payments: "))
gross_income = float(input("Enter gross monthly income: "))

if monthly_debt > 0 and gross_income > 0:
    ratio = (monthly_debt / gross_income) * 100
    print("Debt-to-income ratio:", round(ratio, 2), "%")

    if ratio < 40:
        print("The debt-to-income ratio is below 40%.")
    else:
        print("The debt-to-income ratio is NOT below 40%.")
else:
    print("Both values must be positive numbers.")
