# 피보나치 수열

import sys

pinaryNum = [0, 1, 1]

for i in range(3, 91):
    pinaryNum.append(pinaryNum[i-2] + pinaryNum[i-1])

n = int(sys.stdin.readline().rstrip())

print(pinaryNum[n])