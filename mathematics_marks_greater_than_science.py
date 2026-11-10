# Check whether mathematics marks are greater than science marks
# Method 1: Normal method
maths = float(input("Enter mathematics marks: "))
science = float(input("Enter science marks: "))
if maths > science:
    print("Mathematics marks are greater than science marks.")

# Method 2: Function method
def compare_marks(maths, science):
    if maths > science:
        print("Mathematics marks are greater than science marks.")

maths = float(input("Enter mathematics marks: "))
science = float(input("Enter science marks: "))
compare_marks(maths, science)
