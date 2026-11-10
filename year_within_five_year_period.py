# Check whether a year falls within a specified five-year period
# The starting and ending years are included.
# Method 1: Normal method
year = int(input("Enter the year to check: "))
start_year = int(input("Enter the starting year: "))
if start_year <= year <= start_year + 4:
    print("The year falls within the five-year period.")

# Method 2: Function method
def check_five_year_period(year, start_year):
    if start_year <= year <= start_year + 4:
        print("The year falls within the five-year period.")

year = int(input("Enter the year to check: "))
start_year = int(input("Enter the starting year: "))
check_five_year_period(year, start_year)
