# Bronze 3

import sys

b_len = int(sys.stdin.readline().rstrip())
b_consist = list(map(int, sys.stdin.readline().split()))

a = [b_consist[0]]

for i in range(1, len(b_consist)):
    temp = (i+1)*b_consist[i]-i*b_consist[i-1]
    a.append(temp)

print(*a, sep=' ')



