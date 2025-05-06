/*
✅ Problem: Sort a nearly sorted array where every element is at most K positions away from its target position.

⚙️ Expected Functionality:
- Input: [6, 5, 3, 2, 8, 10, 9], K = 3
- Output: [2, 3, 5, 6, 8, 9, 10]

🚫 Restrictions:
- Do NOT use full sort.
- Use a min-heap to keep track of K elements efficiently.

💡 Working Logic:
- Use a priority queue (min-heap).
- Push first K+1 elements and then insert+remove one by one to build sorted output.

🧠 Write your implementation below this comment:
*/
