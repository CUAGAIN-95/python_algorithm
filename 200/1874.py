import sys

n = int(sys.stdin.readline())
nums = list(range(n, 0, -1))
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
stack = []
result = ""
for j in arr:
    while len(stack) == 0 or stack[-1] < j:
        stack.append(nums.pop())
        result += "+"
    if stack[-1] > j:
        result = "NO"
        break
    if stack[-1] == j:
        stack.pop()
        result += "-"
if result == "NO":
    print(result)
else:
    for i in result:
        print(i)
