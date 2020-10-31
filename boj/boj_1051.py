# Silver 3

import sys

n, m = map(int, sys.stdin.readline().split())

square = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

side = min(n, m)

res = 0

# 세로
for i in range(n):
    # 가로
    for j in range(m):
        # 한 변의 길이를 최대 side까지 늘려가면서 체크
        for s in range(side):
            if (i+s < n and j+s < m) and (square[i][j] == square[i+s][j] and square[i][j] == square[i][j+s] and square[i][j] == square[i+s][j+s]):
                if s > res:
                    res = s

print((res+1)**2)