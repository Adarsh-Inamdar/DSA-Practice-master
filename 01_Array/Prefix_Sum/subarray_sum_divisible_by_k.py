"""
✅ Problem: Count the number of subarrays whose sum is divisible by K.

⚙️ Expected Functionality:
- Input: arr = [4, 5, 0, -2, -3, 1], K = 5
- Output: 7 subarrays

🚫 Restrictions:
- Do NOT use nested loops.
- Must use prefix sum and hashmap to achieve O(N) solution.

💡 Working Logic:
- Track prefix sum and mod values.
- Use a hashmap to store frequency of each mod.
- Handle negative mods by converting them to positive (i.e., ((sum % K) + K) % K)

🧠 Write your implementation below this comment:
"""

