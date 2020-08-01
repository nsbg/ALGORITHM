# Silver 5

import sys

t = int(input())

for i in range(t):
    num = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

    print(num[2])