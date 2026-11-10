# Check whether a person qualifies for a family ticket
# A person qualifies if they are below 12 or accompanied by a parent.
# Method 1: Normal method
age = int(input("Enter age: "))
parent_input = input("Is the person accompanied by a parent? (yes/no): ").lower()
if age < 12 or parent_input == "yes":
    print("The person qualifies for a family ticket.")

# Method 2: Function method
def check_family_ticket(age, parent_input):
    if age < 12 or parent_input == "yes":
        print("The person qualifies for a family ticket.")

age = int(input("Enter age: "))
parent_input = input("Is the person accompanied by a parent? (yes/no): ").lower()
check_family_ticket(age, parent_input)
