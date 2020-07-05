# Bronze 3

import sys

n = int(sys.stdin.readline().rstrip())

c = sorted(list(map(int, sys.stdin.readline().split())))

print(sum(c)-c[len(c)-1])
