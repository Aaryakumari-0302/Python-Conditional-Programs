# Check whether a student scores at least 90 in any two of three subjects
# Method 1: Normal method
subject1 = float(input("Enter marks in subject 1: "))
subject2 = float(input("Enter marks in subject 2: "))
subject3 = float(input("Enter marks in subject 3: "))
count = (subject1 >= 90) + (subject2 >= 90) + (subject3 >= 90)
if count >= 2:
    print("The student qualifies for a performance award.")

# Method 2: Function method
def check_performance_award(subject1, subject2, subject3):
    count = (subject1 >= 90) + (subject2 >= 90) + (subject3 >= 90)
    if count >= 2:
        print("The student qualifies for a performance award.")

subject1 = float(input("Enter marks in subject 1: "))
subject2 = float(input("Enter marks in subject 2: "))
subject3 = float(input("Enter marks in subject 3: "))
check_performance_award(subject1, subject2, subject3)
