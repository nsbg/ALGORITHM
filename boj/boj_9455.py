# Bronze 1

import sys

t = int(sys.stdin.readline().rstrip())

cnt = 0

for i in range(t):
    m, n = map(int, sys.stdin.readline().split())

    for j in range(m):
        row = input().split()