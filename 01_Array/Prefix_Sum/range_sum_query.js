/*
✅ Problem: Answer multiple queries asking the sum of elements from index L to R.

⚙️ Expected Functionality:
- Input: arr = [1, 2, 3, 4, 5]
- Query: sum from index 1 to 3 → Output: 9 (2+3+4)

🚫 Restrictions:
- Do NOT use loops inside queries.
- Preprocess prefix sum array for O(1) query time.

💡 Working Logic:
- Build prefix array.
- For each query, return prefix[r] - prefix[l-1] (handle l = 0 separately)

🧠 Write your implementation below this comment:
*/
