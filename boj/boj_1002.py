# Silver 4

import sys

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    d = ((x1-x2)**2+(y1-y2)**2)**(1/2)

    r = [d, r1, r2]

    if d == 0 and r1 == r2:
        print(-1)
    elif max(r) > sum(r)-max(r):
        print(0)
    elif r1+r2 == d or abs(r1-r2) == d:
        print(1)
    else:
        print(2)