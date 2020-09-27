# Silver 4

import sys

n = int(sys.stdin.readline().rstrip())

res = 0

numList = []

for i in range(n):
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        del numList[-1]
    else:
        numList.append(num)

print(sum(numList))