# Bronze 1

import sys

# n : 세로 줄, m : 가로 줄
n, m = map(int, sys.stdin.readline().split())

numList = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

k = int(input())

# 배열 인덱스 1부터 시작하려고 n, m에 1씩 더한 크기로 생성
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i][j-1]+numList[i-1][j-1]+dp[i-1][j]-dp[i-1][j-1]
print(dp)

# for _ in range(k):
#     i, j, x, y = map(int, sys.stdin.readline().split())

#     result = 0
    
#     if i == x and j == y:
#         result = numList[i-1][j-1]
#     else:
#         for row in range(i-1, x):
#             for col in range(j-1, y):
#                 result += numList[row][col]

#     print(result)