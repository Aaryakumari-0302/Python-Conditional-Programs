# Program: Classify a computer's RAM capacity
# Basic (up to 4 GB), Standard (8 GB), High (16 GB or more)
# Any other value (for example 5, 6, 7 GB) is Unsupported

# ---------- INPUT (used by both solutions) ----------
ram = int(input("Enter RAM capacity (GB): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if ram > 0 and ram <= 4:
    print("RAM type: Basic")
elif ram == 8:
    print("RAM type: Standard")
elif ram >= 16:
    print("RAM type: High")
else:                                # 0, negative, or values like 5, 6, 7, 9...15
    print("RAM type: Unsupported")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_ram(gb):
    # Returns the RAM type
    if gb > 0 and gb <= 4:
        return "Basic"
    elif gb == 8:
        return "Standard"
    elif gb >= 16:
        return "High"
    else:
        return "Unsupported"

result = classify_ram(ram)
print("RAM type:", result)
