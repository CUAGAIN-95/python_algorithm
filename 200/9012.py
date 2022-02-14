import sys

n = int(sys.stdin.readline())
for _ in range(n):
    PS = sys.stdin.readline()
    count = 0
    for i in PS:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count == -1:
            break
    if count != 0:
        print("NO")
    else:
        print("YES")
