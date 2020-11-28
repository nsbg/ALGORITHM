# Silver 3

import sys

num = [0, 1, 2]

for i in range(3, 1001):
    num.append(num[i-2]+num[i-1])

n = int(input())

print(num[n] % 10007)