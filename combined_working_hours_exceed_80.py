# Check whether two employees work more than 80 hours combined per week
# Method 1: Normal method
hours1 = float(input("Enter first employee's weekly hours: "))
hours2 = float(input("Enter second employee's weekly hours: "))
if hours1 + hours2 > 80:
    print("The combined working hours exceed 80.")

# Method 2: Function method
def check_working_hours(hours1, hours2):
    if hours1 + hours2 > 80:
        print("The combined working hours exceed 80.")

hours1 = float(input("Enter first employee's weekly hours: "))
hours2 = float(input("Enter second employee's weekly hours: "))
check_working_hours(hours1, hours2)
