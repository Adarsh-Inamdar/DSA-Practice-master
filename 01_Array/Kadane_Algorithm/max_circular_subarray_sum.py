/*
✅ Problem: Find the maximum sum of a circular subarray.

⚙️ Expected Functionality:
- The array wraps around, so the end and start can be part of the same subarray.
- Input: [8, -1, 3, 4]
- Output: 15 (as 3+4+8)

🚫 Restrictions:
- Do NOT use array concatenation or circular traversal using shift().
- Must be solved using Kadane's algorithm and a clever trick.

💡 Working Logic:
- Case 1: Max subarray using normal Kadane.
- Case 2: Invert elements → run Kadane → subtract from total sum.

🧠 Write your implementation below this comment:
*/
