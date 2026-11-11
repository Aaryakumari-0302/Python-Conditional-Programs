# Program: Classify a number as a multiple of 4, a multiple of 6, or neither
# Rule: check the multiple of 4 first

# ---------- INPUT (used by both solutions) ----------
number = int(input("Enter a number: "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if number % 4 == 0:                  # check multiple of 4 first
    print(number, "is a multiple of 4")
elif number % 6 == 0:                # then check multiple of 6
    print(number, "is a multiple of 6")
else:                                # neither
    print(number, "is a multiple of neither 4 nor 6")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_number(num):
    # This function returns a message for the given number
    if num % 4 == 0:
        return "Multiple of 4"
    elif num % 6 == 0:
        return "Multiple of 6"
    else:
        return "Multiple of neither 4 nor 6"

result = classify_number(number)     # call the function
print(number, "->", result)
