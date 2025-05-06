/*
✅ Problem: Count how many times a given element appears in a sorted array.

⚙️ Expected Functionality:
- Input: arr = [1, 2, 2, 2, 3, 4], target = 2
- Output: 3

🚫 Restrictions:
- Do NOT use loops to count occurrences linearly.
- Use Binary Search to find first and last position of the element.

💡 Working Logic:
- Use two binary searches:
  1. To find the first occurrence of the element.
  2. To find the last occurrence.
- Count = (last - first + 1)

🧠 Write your implementation below this comment:
*/
