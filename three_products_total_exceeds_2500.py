# Check whether the total price of three products exceeds Rs. 2,500
# Method 1: Normal method
price1 = float(input("Enter price of first product: "))
price2 = float(input("Enter price of second product: "))
price3 = float(input("Enter price of third product: "))
if price1 + price2 + price3 > 2500:
    print("The total price exceeds Rs. 2,500.")

# Method 2: Function method
def check_total_price(price1, price2, price3):
    if price1 + price2 + price3 > 2500:
        print("The total price exceeds Rs. 2,500.")

price1 = float(input("Enter price of first product: "))
price2 = float(input("Enter price of second product: "))
price3 = float(input("Enter price of third product: "))
check_total_price(price1, price2, price3)
