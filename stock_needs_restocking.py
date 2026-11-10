# Check whether a product's stock quantity is below 10
# Method 1: Normal method
quantity = int(input("Enter stock quantity: "))
if quantity < 10:
    print("The product needs restocking.")

# Method 2: Function method
def check_stock(quantity):
    if quantity < 10:
        print("The product needs restocking.")

quantity = int(input("Enter stock quantity: "))
check_stock(quantity)
