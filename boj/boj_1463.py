# Silver 3

import sys

n = int(sys.stdin.readline().strip())

dp = [0]*1000001

for i in range(2, 1000001):
    if (i == 2) or (i == 3):
        dp[i] = 1
    else:
        dp[i] = dp[i-1]+1
        
        if i%2 == 0:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3 == 0:
            dp[i] = min(dp[i//3]+1, dp[i])
        
print(dp[n])