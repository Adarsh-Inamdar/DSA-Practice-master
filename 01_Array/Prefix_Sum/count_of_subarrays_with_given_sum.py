"""
✅ Problem: Count the number of subarrays that sum up to a given value `K`.

⚙️ Expected Functionality:
- Input: arr = [1, 2, 3], K = 3
- Output: 2 (subarrays: [1,2] and [3])

🚫 Restrictions:
- Do NOT use nested loops.
- Must use prefix sum and hashmap to get O(N) solution.

💡 Working Logic:
- Use a hashmap to store frequency of prefix sums.
- At each index, check if (currentPrefixSum - K) exists in the map.

🧠 Write your implementation below this comment:
"""

