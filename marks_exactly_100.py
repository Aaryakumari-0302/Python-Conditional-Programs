# Check whether a student's marks are exactly 100
# Method 1: Normal method
marks = float(input("Enter marks: "))
if marks == 100:
    print("The student's marks are exactly 100.")

# Method 2: Function method
def check_marks(marks):
    if marks == 100:
        print("The student's marks are exactly 100.")

marks = float(input("Enter marks: "))
check_marks(marks)
