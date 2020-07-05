# Bronze 4

import sys

a, b, c, d = map(int, sys.stdin.readline().split(' '))

print(abs((a+d)-(b+c)))