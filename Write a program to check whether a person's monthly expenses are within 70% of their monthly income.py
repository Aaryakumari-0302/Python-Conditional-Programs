# Check whether a person's monthly expenses are within 70% of their monthly income

income = float(input("Enter monthly income: "))
expenses = float(input("Enter monthly expenses: "))

limit = income * 70 / 100
print("70% of income is:", limit)

if expenses <= limit:
    print("Expenses are within 70% of the monthly income.")
else:
    print("Expenses are more than 70% of the monthly income.")
