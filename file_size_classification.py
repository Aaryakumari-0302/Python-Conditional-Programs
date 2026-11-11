# Program: Classify a file size
# Small (below 1 MB), Medium (1-10 MB), Large (above 10 MB)

# ---------- INPUT (used by both solutions) ----------
size = float(input("Enter file size (MB): "))

# =====================================================
# SOLUTION 1: NORMAL METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 1: Normal Method ---")

if size < 1:
    print("File size: Small")
elif size <= 10:                     # 1 to 10 (both included)
    print("File size: Medium")
else:                                # above 10
    print("File size: Large")

# =====================================================
# SOLUTION 2: FUNCTION METHOD (if-elif-else)
# =====================================================
print("\n--- Solution 2: Function Method ---")

def classify_file_size(mb):
    # Returns the file size category
    if mb < 1:
        return "Small"
    elif mb <= 10:
        return "Medium"
    else:
        return "Large"

result = classify_file_size(size)
print("File size:", result)
