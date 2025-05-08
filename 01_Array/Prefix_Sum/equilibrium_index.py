"""
✅ Problem: Find the index where the sum of elements on the left is equal to the sum on the right.

⚙️ Expected Functionality:
- Input: arr = [-7, 1, 5, 2, -4, 3, 0]
- Output: 3 (index 3 is equilibrium)

🚫 Restrictions:
- Do NOT use extra space except variables (no prefix arrays).
- Must be solved in one pass after computing total sum.

💡 Working Logic:
- First calculate total sum.
- Traverse again while maintaining leftSum.
- At each index, check if leftSum == totalSum - leftSum - arr[i]

🧠 Write your implementation below this comment:
"""

