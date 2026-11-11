# Check whether a given character is a vowel or not, ignoring case

ch = input("Enter a single character: ")

# Convert to lowercase so 'A' and 'a' are treated the same
ch = ch.lower()

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("The character is a vowel.")
    else:
        print("The character is not a vowel.")
