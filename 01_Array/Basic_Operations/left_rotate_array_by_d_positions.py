"""
✅ Problem: Rotate the given array to the left by D positions.

⚙️ Expected Functionality:
- Given an array of size N and an integer D (0 <= D < N),
  rotate the array elements to the left by D positions.
  e.g., arr = [1, 2, 3, 4, 5], D = 2 → Output: [3, 4, 5, 1, 2]

🚫 Restrictions:
- Do NOT use built-in methods like array.slice(), array.splice(), or array.concat().
- Do NOT use array.reverse().
- Do NOT use temporary arrays longer than D elements.
- Must be done in O(N) time and O(1) extra space (or O(D) if unavoidable).

💡 Working Logic:
- Step 1: Store the first D elements in a temporary array.
- Step 2: Shift the remaining N - D elements to the left.
- Step 3: Append the stored D elements to the end of the array.

🧠 Write your implementation below this comment:
"""

D = int(input("Enter by how much to shift:"))
arr = [1,2,3,4,5]
b = []
for i in range(D,5):
    b.append(arr[i])

for x in range(0,D):
    b.append(arr[x])
print(b)