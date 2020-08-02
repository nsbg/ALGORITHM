# Silver 1

import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0
total = k

coin = sorted([int(sys.stdin.readline().rstrip()) for i in range(n)], reverse=True)

for c in coin:
    if total == 0:
        break
    else:
        if total >= c:
            chk = total // c
            cnt += chk

            total -= (chk*c)

print(cnt)