# Check whether a student has passed an examination:
# total marks at least 200 out of 300 AND no subject mark below 35

m1 = int(input("Enter marks of subject 1 (out of 100): "))
m2 = int(input("Enter marks of subject 2 (out of 100): "))
m3 = int(input("Enter marks of subject 3 (out of 100): "))

total = m1 + m2 + m3
print("Total marks:", total, "out of 300")

if total >= 200 and m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("The student has passed.")
else:
    print("The student has failed.")
