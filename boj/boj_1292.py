# Silver 4

import sys

a, b = map(int, sys.stdin.readline().split())

num = []

for i in range(1, 46):
    num += [i] * i

print(sum(num[a-1:b]))