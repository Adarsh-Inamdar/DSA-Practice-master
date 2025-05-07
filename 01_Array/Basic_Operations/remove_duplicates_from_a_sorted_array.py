# ✅ Problem: Remove duplicates from a sorted array and return the length of unique elements.

# ⚙️ Expected Functionality:
# - Input: [1, 1, 2, 2, 3, 4]
# - Output: [1, 2, 3, 4] (first 4 elements), return 4

# 🚫 Restrictions:
# - Do NOT use Set or Map.
# - Do NOT use additional arrays.
# - Must be done in-place with O(1) extra space.

# 💡 Working Logic:
# - Use two-pointer technique.
# - `i` points to the last unique element found.
# - `j` iterates through the array.
# - When arr[i] != arr[j], increment i and copy arr[j] to arr[i].

# 🧠 Write your implementation below this comment:

