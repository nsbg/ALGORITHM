# Silver 4

import sys

n, m = map(int, sys.stdin.readline().split())

nSet = set()
mSet = set()

for i in range(n):
    nSet.add(sys.stdin.readline().rstrip())

for j in range(m):
    mSet.add(sys.stdin.readline().rstrip())

setIntersection = sorted(list(nSet&mSet))

for s in setIntersection:
    print(s)