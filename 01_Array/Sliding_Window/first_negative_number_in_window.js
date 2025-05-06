/*
✅ Problem: For every window of size K, print the first negative number in that window.

⚙️ Expected Functionality:
- Input: arr = [12, -1, -7, 8, -15, 30, 16, 28], K = 3
- Output: [-1, -1, -7, -15, -15, 0] (use 0 when no negative number)

🚫 Restrictions:
- Do NOT use nested loops.
- Must solve using an optimized sliding window technique (queue or deque).

💡 Working Logic:
- Use a deque to store indices of negative numbers.
- As window slides, add new negatives and remove out-of-window ones.

🧠 Write your implementation below this comment:
*/
