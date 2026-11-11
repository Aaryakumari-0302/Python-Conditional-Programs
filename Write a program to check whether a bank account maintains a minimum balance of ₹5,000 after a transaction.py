# Check whether a bank account maintains a minimum balance of Rs 5,000 after a transaction

balance = float(input("Enter current balance: "))
amount = float(input("Enter transaction amount (positive = deposit, negative = withdrawal): "))

new_balance = balance + amount
print("Balance after transaction: Rs", new_balance)

if new_balance >= 5000:
    print("The account maintains the minimum balance of Rs 5,000.")
else:
    print("The account does NOT maintain the minimum balance of Rs 5,000.")
