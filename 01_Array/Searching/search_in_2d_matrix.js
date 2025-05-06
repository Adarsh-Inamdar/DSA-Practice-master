/*
✅ Problem: Search for a target value in a 2D matrix where:
- Each row is sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

⚙️ Expected Functionality:
- Input: matrix = [[1,3,5],[7,9,11]], target = 9
- Output: true

🚫 Restrictions:
- Do NOT flatten the array or use filter/find.
- Must treat it as a binary search problem in 2D.

💡 Working Logic:
- Treat the 2D array as a 1D sorted array and use binary search.
- Convert 1D mid index to 2D using: row = mid / cols, col = mid % cols

🧠 Write your implementation below this comment:
*/
