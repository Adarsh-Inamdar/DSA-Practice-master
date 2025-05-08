"""
✅ Problem: Check if there exists a subarray whose sum is 0.

⚙️ Expected Functionality:
- Input: arr = [4, 2, -3, 1, 6]
- Output: true (subarray [2, -3, 1] sums to 0)

🚫 Restrictions:
- Do NOT use nested loops.
- Must use prefix sum and hashmap for O(N) time.

💡 Working Logic:
- Keep track of prefix sum at every step.
- If prefix sum is 0 or has occurred before → subarray with 0 sum exists.

🧠 Write your implementation below this comment:
"""

