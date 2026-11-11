# Check whether a product's selling price is greater than its cost price

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    print("The selling price is greater than the cost price (profit).")
else:
    print("The selling price is not greater than the cost price.")
