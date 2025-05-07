# ✅ Problem: Move all 0s in the array to the end, maintaining the order of non-zero elements.

# ⚙️ Expected Functionality:
# - Input: [0, 1, 0, 3, 12]
# - Output: [1, 3, 12, 0, 0]

# 🚫 Restrictions:
# - Do NOT use built-in filter(), sort(), or array copying.
# - Do NOT use new arrays to store results (must do in-place).

# 💡 Working Logic:
# - Use two-pointer approach.
# - Pointer `j` tracks the position of the next non-zero.
# - Traverse the array: if arr[i] is not zero, swap it with arr[j] and increment j.

# 🧠 Write your implementation below this comment:

