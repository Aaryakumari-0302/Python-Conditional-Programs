# Check whether a customer qualifies for a refund
# Rule: returned within 7 days AND the item is unused

days = int(input("Enter number of days since purchase: "))
unused = input("Is the item unused? (yes/no): ")

if days <= 7 and unused.lower() == "yes":
    print("The customer qualifies for a refund.")
else:
    print("The customer does not qualify for a refund.")
