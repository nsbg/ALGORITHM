import sys

n = int(sys.stdin.readline().rstrip())

r = []

for i in range(n):
    s = sys.stdin.readline().split()
    r.append(s)

    if sum(r[i]) != 0:
        

