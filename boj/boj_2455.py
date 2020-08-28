# Bronze 3

import sys

res = 0
m = 0

for i in range(4):
    minus, plus = map(int, sys.stdin.readline().split())

    res += plus
    res -= minus

    if res > m:
        m = res

print(m)