# Bronze 1

import sys

M = int(input())
N = int(input())

total = 0
minimum = 10000

squared = [0, 1, 4, 5, 6, 9]

for i in range(M, N+1):
    if i**0.5 == int(i**0.5):
        total += i

        if i < minimum:
            minimum = min(i, minimum) 

if total == 0:
    print("-1")
else:
    print(total, minimum, end='\n')