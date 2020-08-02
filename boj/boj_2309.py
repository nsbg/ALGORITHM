# Bronze 2
# Brute-force

import sys

height = list(map(int, [sys.stdin.readline().rstrip() for i in range(9)]))

f = sum(height)-100

one = 0
two = 0

for i in range(8):
    for j in range(i+1, 9):
        if height[i]+height[j] == f:
            one = height[i]
            two = height[j]

height.remove(one)
height.remove(two)

for d in sorted(height):
    print(d)
