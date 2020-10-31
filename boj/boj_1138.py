# Silver 2

import sys

n = int(input())

p = list(map(int, sys.stdin.readline().split()))

order = []

for i in range(n):
    # 배열 마지막 인덱스는 n-1
    order.insert(p[(n-1)-i], n-i)

print(*order, sep=' ')