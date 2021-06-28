# Silver 3

import sys

n = int(input())

stair = [0 for i in range(n+1)]

# dp(n) : n칸까지 올랐을 때 얻을 수 있는 최댓값
dp = [0 for i in range(n+1)]

for i in range(1, n+1):
    stair[i] = int(input())

dp[1] = stair[1]
dp[2] = stair[1]+stair[2]
dp[3] = max(stair[3]+stair[2], stair[3]+stair[1])

for j in range(4, n+1):
    dp[j] = max(stair[j]+dp[j-2], stair[j]+stair[j-1]+dp[j-3])

print(dp[n])