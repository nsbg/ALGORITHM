# Silver 1

import sys
import math

N = int(sys.stdin.readline().strip())

is_prime = [True for i in range(1005000)]

is_prime[1] = False

for i in range(2, int(math.sqrt(1005000))+1):
    if is_prime[i] == True:
        for j in range(i+i, 1005000, i):
            is_prime[j] = False

prime = [i for i in range(N, 1005000) if is_prime[i] == True]

for p in prime:
    if str(p) == str(p)[::-1]:
        print(p)
        break