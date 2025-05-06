/*
✅ Problem: Given an array of elevations, find how much water it can trap after raining.

⚙️ Expected Functionality:
- Input: [0,1,0,2,1,0,1,3,2,1,2,1]
- Output: 6

🚫 Restrictions:
- Do NOT use nested loops.
- Use two-pointer or prefix-max/suffix-max optimization.

💡 Working Logic:
- Use two pointers and track leftMax and rightMax.
- Water trapped = min(leftMax, rightMax) - current height.

🧠 Write your implementation below this comment:
*/
