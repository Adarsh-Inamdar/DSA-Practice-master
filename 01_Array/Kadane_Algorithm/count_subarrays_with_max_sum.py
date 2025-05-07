"""
✅ Problem: Count the number of subarrays that achieve the maximum subarray sum.

⚙️ Expected Functionality:
- Given an integer array, count how many contiguous subarrays have the maximum sum.
- Input: [1, -1, 2, 2, -1]
- Output: Count of subarrays with max sum (e.g., 1 subarray [2, 2] → max sum 4)

🚫 Restrictions:
- Do NOT use built-in functions like reduce(), filter(), or map().
- Must run in linear time, O(N), and use O(1) extra space if possible.

💡 Working Logic:
- Use Kadane’s algorithm to find the maximum subarray sum.
- Then iterate again to count subarrays matching that sum.

🧠 Write your implementation below this comment:
"""

