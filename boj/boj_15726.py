# Bronze 4

import sys

a, b, c = map(int, sys.stdin.readline().split())

first = a/b * c
second = a*b / c

if first > second:
    print(int(first))
else:
    print(int(second))