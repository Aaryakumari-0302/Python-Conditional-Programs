# Program: Display a message for a battery level
# Low (below 20%), Medium (20-79%), High (80-100%)

# ---------- INPUT (used by both solutions) ----------
battery = float(input("Enter battery level (%): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if battery < 20:
    print("Battery is LOW. Please charge your device.")
elif battery < 80:                   # 20 up to 79.99
    print("Battery is MEDIUM.")
else:                                # 80 to 100
    print("Battery is HIGH.")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def battery_message(level):
    # Returns a message for the battery level
    if level < 20:
        return "Battery is LOW. Please charge your device."
    elif level < 80:
        return "Battery is MEDIUM."
    else:
        return "Battery is HIGH."

message = battery_message(battery)
print(message)
