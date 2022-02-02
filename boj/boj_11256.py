# Silver 5

import sys

T = int(input())

for _ in range(T):
    J, N = map(int, sys.stdin.readline().split())

    cnt = 0
    tmp = 0

    mul = []
    
    for _ in range(N):
        R, C = map(int, sys.stdin.readline().split())
        
        mul.append(R*C)

    for m in sorted(mul, reverse=True):
        J -= m
        cnt += 1

        if J <= 0:
            break

    print(cnt)