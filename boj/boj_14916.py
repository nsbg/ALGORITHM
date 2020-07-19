# Silver 5

import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0

if n < 0 or n == 1 or n == 3:
    print("-1")

while n > 0:
    if n % 5 == 0:
        print(cnt + n // 5)
        break
    else:
        n -= 2
        cnt += 1