# Check whether a date falls on a weekend
# Weekday numbers: 1 = Monday, 2 = Tuesday, ... 6 = Saturday, 7 = Sunday

weekday = int(input("Enter the weekday number (1 to 7): "))

if weekday >= 1 and weekday <= 7:
    if weekday == 6 or weekday == 7:
        print("The date falls on a weekend.")
    else:
        print("The date does not fall on a weekend.")
else:
    print("Invalid weekday number. Please enter a number from 1 to 7.")
