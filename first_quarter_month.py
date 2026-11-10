# Check whether a month number belongs to the first quarter
# Method 1: Normal method
month = int(input("Enter month number (1-12): "))
if 1 <= month <= 3:
    print("The month belongs to the first quarter.")

# Method 2: Function method
def check_first_quarter(month):
    if 1 <= month <= 3:
        print("The month belongs to the first quarter.")

month = int(input("Enter month number (1-12): "))
check_first_quarter(month)
