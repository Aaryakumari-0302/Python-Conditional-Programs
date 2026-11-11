# Program: Classify an internet connection speed
# Slow (below 10 Mbps), Moderate (10-50 Mbps),
# Fast (above 50 up to 100 Mbps), Very Fast (above 100 Mbps)

# ---------- INPUT (used by both solutions) ----------
speed = float(input("Enter internet speed (Mbps): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if speed < 10:
    print("Internet speed: Slow")
elif speed <= 50:                    # 10 to 50
    print("Internet speed: Moderate")
elif speed <= 100:                   # above 50 up to 100
    print("Internet speed: Fast")
else:                                # above 100
    print("Internet speed: Very Fast")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_speed(mbps):
    # Returns the internet speed category
    if mbps < 10:
        return "Slow"
    elif mbps <= 50:
        return "Moderate"
    elif mbps <= 100:
        return "Fast"
    else:
        return "Very Fast"

result = classify_speed(speed)
print("Internet speed:", result)
