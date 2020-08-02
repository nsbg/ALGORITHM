# Silver 3

import sys

n = int(input())

time = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    if i == 0:
        time[i]
    else:
        time[i] = time[i-1]+time[i]

print(sum(time))