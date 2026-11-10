# Check whether a person is below 5 years old
# Method 1: Normal method
age = int(input("Enter age: "))
if age < 5:
    print("The person qualifies for the toddler category.")

# Method 2: Function method
def check_toddler(age):
    if age < 5:
        print("The person qualifies for the toddler category.")

age = int(input("Enter age: "))
check_toddler(age)
