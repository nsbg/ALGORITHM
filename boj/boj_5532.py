# Bronze 4

import sys

# 방학 일수, 풀어야하는 국어, 풀어야하는 수학, 최대 풀 수 있는 국어, 최대 풀 수 있는 수학
l = int(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())
d = int(sys.stdin.readline().rstrip())

res = 0

if a // c > b // d:
    if a % c == 0:
        res = a // c
    else:
        res = (a // c) + 1
else:
    if b % d == 0:
        res = b // d
    else:
        res = (b // d) + 1

if l-res > 0:
    print(l-res)
else:
    print("0")