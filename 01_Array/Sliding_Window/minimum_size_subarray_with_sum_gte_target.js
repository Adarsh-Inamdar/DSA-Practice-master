/*
✅ Problem: Find the minimum length of a contiguous subarray of which the sum ≥ target.

⚙️ Expected Functionality:
- Input: arr = [2,3,1,2,4,3], target = 7
- Output: 2 (subarray: [4,3])

🚫 Restrictions:
- Do NOT check all possible subarrays.
- Must use sliding window technique with two pointers.

💡 Working Logic:
- Use two pointers and expand right pointer to add to sum.
- Once sum ≥ target, move left pointer to minimize window.

🧠 Write your implementation below this comment:
*/
