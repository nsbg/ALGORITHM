# Silver 5

import sys

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    cnt = 0
    
    for i in range(N, M+1):
        for n in str(i):
            if n == '0':
                cnt += 1

    print(cnt)    