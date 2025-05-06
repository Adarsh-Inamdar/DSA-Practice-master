"""
✅ Problem: Rotate the given array to the left by one position.

⚙️ Expected Functionality:
- Given an array of size N, rotate it to the left by one position.
  e.g., arr = [10, 20, 30, 40] → Output: [20, 30, 40, 10]

🚫 Restrictions:
- Do NOT use array methods like shift(), unshift(), push(), or slice().
- Do NOT use array.reverse().
- Do NOT use temporary arrays longer than 1 element.

💡 Working Logic:
- Step 1: Store the first element in a temporary variable.
- Step 2: Shift all elements from index 1 to N-1 one position to the left.
- Step 3: Place the first element at the last index.

🧠 Write your implementation below this comment:

"""

D = int(input("Enter by how much to shift:"))
arr = [1,2,3,4,5]

arr[i] = arr[i]+ arr[-1]

print(arr)