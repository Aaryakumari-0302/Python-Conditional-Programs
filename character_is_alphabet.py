# Check whether a character is an English alphabet letter
# Method 1: Normal method
character = input("Enter one character: ")
if len(character) == 1 and (("A" <= character <= "Z") or ("a" <= character <= "z")):
    print("It is an alphabet.")

# Method 2: Function method
def check_alphabet(character):
    if len(character) == 1 and (("A" <= character <= "Z") or ("a" <= character <= "z")):
        print("It is an alphabet.")

character = input("Enter one character: ")
check_alphabet(character)
