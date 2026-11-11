# Program: Classify a website response time
# Excellent (below 200 ms), Good (200-500 ms),
# Slow (above 500 up to 1000 ms), Very Slow (above 1000 ms)

# ---------- INPUT (used by both solutions) ----------
time_ms = float(input("Enter response time (ms): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if time_ms < 200:
    print("Response time: Excellent")
elif time_ms <= 500:                 # 200 to 500
    print("Response time: Good")
elif time_ms <= 1000:                # above 500 up to 1000
    print("Response time: Slow")
else:                                # above 1000
    print("Response time: Very Slow")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_response_time(ms):
    # Returns the response time category
    if ms < 200:
        return "Excellent"
    elif ms <= 500:
        return "Good"
    elif ms <= 1000:
        return "Slow"
    else:
        return "Very Slow"

result = classify_response_time(time_ms)
print("Response time:", result)
