import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(range(1, n + 1))
result = []
i = 0
while arr:
    i += k - 1
    i %= len(arr)
    result.append(str(arr.pop(i)))

print("<" + ", ".join(result) + ">")
