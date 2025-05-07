"""
✅ Problem: Remove duplicates from a sorted array and return the length of unique elements.

⚙️ Expected Functionality:
- Input: [1, 1, 2, 2, 3, 4]
- Output: [1, 2, 3, 4] (first 4 elements), return 4

🚫 Restrictions:
- Do NOT use Set or Map.
- Do NOT use additional arrays.
- Must be done in-place with O(1) extra space.

💡 Working Logic:
- Use two-pointer technique.
- `i` points to the last unique element found.
- `j` iterates through the array.
- When arr[i] != arr[j], increment i and copy arr[j] to arr[i].

🧠 Write your implementation below this comment:

"""

def count_digits(arr):
    count = {i: 0 for i in range(10)}
    
    switch = {
        0: lambda: count.update({0: count[0] + 1}),
        1: lambda: count.update({1: count[1] + 1}),
        2: lambda: count.update({2: count[2] + 1}),
        3: lambda: count.update({3: count[3] + 1}),
        4: lambda: count.update({4: count[4] + 1}),
        5: lambda: count.update({5: count[5] + 1}),
        6: lambda: count.update({6: count[6] + 1}),
        7: lambda: count.update({7: count[7] + 1}),
        8: lambda: count.update({8: count[8] + 1}),
        9: lambda: count.update({9: count[9] + 1}),
    }

    for num in arr:
        if num in switch:
            switch[num]()

    print("Digits that appeared at least once:")
    for digit in range(10):
        if count[digit] > 0:
            print(digit)

arr = [1, 1, 2, 2, 3, 4]
count_digits(arr)
