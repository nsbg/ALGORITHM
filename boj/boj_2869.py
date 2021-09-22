# Bronze 1

import sys

A, B, V = map(int, sys.stdin.readline().split())

if (V-B)%(A-B) != 0:
    day = (V-B)//(A-B)+1
else:
    day = (V-B)//(A-B)

print(day)