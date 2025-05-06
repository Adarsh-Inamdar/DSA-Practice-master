/*
✅ Problem: Find the length of the longest substring with exactly K unique characters.

⚙️ Expected Functionality:
- Input: str = "aabacbebebe", K = 3
- Output: 7 ("cbebebe")

🚫 Restrictions:
- Do NOT use brute-force or nested loops.
- Use sliding window with a frequency map.

💡 Working Logic:
- Use two pointers to define a window.
- Expand right pointer and maintain a map of characters.
- Shrink left pointer when unique count exceeds K.

🧠 Write your implementation below this comment:
*/
