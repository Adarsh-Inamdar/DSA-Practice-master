'''✅ Problem: Reverse the elements of the array.

⚙️ Expected Functionality:
- Input: [1, 2, 3, 4, 5]
- Output: [5, 4, 3, 2, 1]

🚫 Restrictions:
- Do NOT use array.reverse().
- Do NOT use built-in methods like unshift(), push(), slice(), etc.
- Do NOT use additional arrays (do in-place).

💡 Working Logic:
- Use two pointers: start and end.
- Swap elements at start and end until they meet in the middle.

🧠 Write your implementation below this comment:
'''
def arrayrev():
    rev = []
    arr = []
    n = int(input("Enter the total elements:"))
    print("Enter The list Elements:")
    for i in range(n):
        arr.append(int(input()))
    for j in range(n-1,-1,-1):
        rev.append(arr[j])
    return rev




rev = arrayrev()

print(rev)
