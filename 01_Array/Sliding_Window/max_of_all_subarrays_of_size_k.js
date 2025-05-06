/*
✅ Problem: For each window of size K, find the maximum element.

⚙️ Expected Functionality:
- Input: arr = [1,3,-1,-3,5,3,6,7], K = 3
- Output: [3,3,5,5,6,7]

🚫 Restrictions:
- Do NOT use brute-force (nested loop).
- Must use a deque to maintain max efficiently.

💡 Working Logic:
- Maintain a deque that stores indices in decreasing order of values.
- At each step, the front of deque gives max of the current window.

🧠 Write your implementation below this comment:
*/
