# Gold 5

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

tower = list(map(int, sys.stdin.readline().split()))

stack = []
received = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] <= tower[i]:
            stack.pop()
        else:
            received[i] = stack[-1][0]
            break
         
    stack.append([i+1, tower[i]])

print(*received)