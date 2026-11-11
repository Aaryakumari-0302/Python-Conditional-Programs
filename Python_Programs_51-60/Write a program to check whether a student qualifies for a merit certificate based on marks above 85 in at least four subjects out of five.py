# Check whether a student qualifies for a merit certificate
# Rule: marks above 85 in at least four subjects out of five

count = 0

for i in range(1, 6):
    marks = float(input("Enter marks for subject " + str(i) + ": "))
    if marks > 85:
        count = count + 1

print("Subjects with marks above 85:", count)

if count >= 4:
    print("The student qualifies for a merit certificate.")
else:
    print("The student does not qualify for a merit certificate.")
