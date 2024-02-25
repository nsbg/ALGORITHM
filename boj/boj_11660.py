# Silver 1

import sys

N, M = map(int, sys.stdin.readline().split())

table = []

for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])