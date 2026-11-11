# Check whether the total cost of five items is within a budget of Rs 1,000

total = 0

for i in range(1, 6):
    price = float(input("Enter price of item " + str(i) + ": "))
    total = total + price

print("Total cost: Rs", total)

if total <= 1000:
    print("The total cost is within the budget of Rs 1,000.")
else:
    print("The total cost is over the budget of Rs 1,000.")
