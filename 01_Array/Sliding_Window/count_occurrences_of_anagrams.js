/*
✅ Problem: Count how many times an anagram of a pattern appears in a given text.

⚙️ Expected Functionality:
- Input: text = "forxxorfxdofr", pattern = "for"
- Output: 3 (Anagrams: "for", "orf", "ofr")

🚫 Restrictions:
- Do NOT sort substrings or use regex.
- Must use sliding window and hash maps or arrays for frequency count.

💡 Working Logic:
- Use a frequency map for the pattern.
- Slide a window of size equal to the pattern across the text.
- Check if frequency maps match at each step.

🧠 Write your implementation below this comment:
*/
