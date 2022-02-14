import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    order = sys.stdin.readline().split()
    if "push" in order:
        stack.append(order[1])
    elif "pop" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
