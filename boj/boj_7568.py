# Silver 5

import sys

N = int(input())

info = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    info.append([x, y])

for i in info:
    cnt = 1

    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    
    print(cnt, end=' ')

