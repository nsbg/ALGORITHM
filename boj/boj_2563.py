# Silver 5

import sys

n = int()

square = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for _ in range(n):
    c, r = map(int, sys.stdin.readline().split())

    for j in range(c, c+10):
        for k in range(r, r+10):
            square[j][k] = 1

for s in square:
    for q in s:
        if q == 1:
            cnt += 1

print(cnt)