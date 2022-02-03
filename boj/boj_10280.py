# Bronze 1

import sys

n, p = map(int, sys.stdin.readline().split())

for i in range(n):
    c, w = sys.stdin.readline().split()

x = n//3+1
y = x+(n-1)//3

if x <= p <= y:
    print("YES")
else:
    print("NO")