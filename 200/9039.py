import sys

n = int(sys.stdin.readline())
for _ in range(n):
    word = sys.stdin.readline().split()
    for i in word:
        print(i[::-1], end=' ')
    print()
