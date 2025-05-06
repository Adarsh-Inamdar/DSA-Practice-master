/*
✅ Problem: Find the length of the longest subarray with sum equal to `K`.

⚙️ Expected Functionality:
- Input: arr = [10, 5, 2, 7, 1, 9], K = 15
- Output: 4 (subarray: [5, 2, 7, 1])

🚫 Restrictions:
- Do NOT use nested loops.
- Must be done in O(N) time using prefix sum and hashmap.

💡 Working Logic:
- Use a hashmap to store first occurrence of prefix sums.
- Track current prefix sum and check if (prefixSum - K) exists.

🧠 Write your implementation below this comment:
*/
