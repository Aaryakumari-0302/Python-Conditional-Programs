# Check whether a customer qualifies for a loyalty reward
# Requirements: at least 10 purchases and spending more than Rs. 20,000.
# Method 1: Normal method
purchases = int(input("Enter number of purchases: "))
amount_spent = float(input("Enter total amount spent: "))
if purchases >= 10 and amount_spent > 20000:
    print("The customer qualifies for a loyalty reward.")

# Method 2: Function method
def check_loyalty_reward(purchases, amount_spent):
    if purchases >= 10 and amount_spent > 20000:
        print("The customer qualifies for a loyalty reward.")

purchases = int(input("Enter number of purchases: "))
amount_spent = float(input("Enter total amount spent: "))
check_loyalty_reward(purchases, amount_spent)
