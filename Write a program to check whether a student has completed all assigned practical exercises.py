# Check whether a student has completed all assigned practical exercises

assigned = int(input("Enter total assigned practical exercises: "))
completed = int(input("Enter number of exercises completed: "))

if completed >= assigned:
    print("The student has completed all assigned practical exercises.")
else:
    print("The student has NOT completed all exercises.")
    print("Remaining exercises:", assigned - completed)
