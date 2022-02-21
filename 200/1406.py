import sys

first_stack = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
second_stack = []
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'L':
        if first_stack:
            second_stack.append(first_stack.pop())
    elif order[0] == 'D':
        if second_stack:
            first_stack.append(second_stack.pop())
    elif order[0] == 'B':
        if first_stack:
            first_stack.pop()
    elif order[0] == 'P':
        first_stack.append(order[1])

print(''.join(first_stack + list(reversed(second_stack))))
