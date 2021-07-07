# Bronze 2

import sys

n = int(input())

for i in range(n):
    name = list(sys.stdin.readline().split())
    name[0] = "god"
    print(''.join(name))