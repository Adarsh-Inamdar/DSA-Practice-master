/*
✅ Problem: Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai),
find two lines that together with the x-axis form a container, such that the container contains the most water.

⚙️ Expected Functionality:
- Input: [1,8,6,2,5,4,8,3,7]
- Output: 49

🚫 Restrictions:
- Do NOT use nested loops (i.e., no brute-force O(n^2)).
- Use two-pointer approach only.

💡 Working Logic:
- Use two pointers at both ends and move inward.
- Calculate area and update max area.
- Move pointer pointing to the smaller height.

🧠 Write your implementation below this comment:
*/
