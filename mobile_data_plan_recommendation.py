# Program: Recommend a mobile data plan based on monthly data usage
# Plans: up to 2 GB, up to 10 GB, up to 30 GB, above 30 GB

# ---------- INPUT (used by both solutions) ----------
usage = float(input("Enter monthly data usage (GB): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if usage <= 2:
    print("Recommended plan: Up to 2 GB plan")
elif usage <= 10:
    print("Recommended plan: Up to 10 GB plan")
elif usage <= 30:
    print("Recommended plan: Up to 30 GB plan")
else:                                # more than 30 GB
    print("Recommended plan: Above 30 GB plan")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def recommend_plan(gb):
    # Returns the plan that suits the usage
    if gb <= 2:
        return "Up to 2 GB plan"
    elif gb <= 10:
        return "Up to 10 GB plan"
    elif gb <= 30:
        return "Up to 30 GB plan"
    else:
        return "Above 30 GB plan"

result = recommend_plan(usage)
print("Recommended plan:", result)
