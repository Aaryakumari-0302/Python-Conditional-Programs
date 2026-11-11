# Check whether a given string is a palindrome, ignoring letter case

text = input("Enter a string: ")

# Convert to lowercase so 'Madam' and 'madam' are treated the same
text = text.lower()

# text[::-1] gives the reversed string
reversed_text = text[::-1]

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
