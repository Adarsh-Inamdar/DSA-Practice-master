/*
✅ Problem: Find the maximum subarray sum after concatenating the array K times.

⚙️ Expected Functionality:
- Input: arr = [1, -2, 1], K = 3
- Concatenated = [1, -2, 1, 1, -2, 1, 1, -2, 1]
- Output: Maximum subarray sum from this new array.

🚫 Restrictions:
- Do NOT actually concatenate the array K times if K is large.
- Must be optimized for large K (up to 10^5).

💡 Working Logic:
- Apply Kadane’s on 1 copy.
- If sum(arr) > 0, answer = max of kadane(2 * arr) + (K - 2) * sum(arr)

🧠 Write your implementation below this comment:
*/
