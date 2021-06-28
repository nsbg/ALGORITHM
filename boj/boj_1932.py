# Silver 1

import sys

triangle = []

n = int(input())

for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split())))

# 원본 데이터(리스트)를 보존해야 하거나 안 간 곳을 체크해야 하는 게 아니면 원본 데이터를 dp 배열로 사용 가능
for j in range(1, n):
    for k in range(j+1):
        # 대각선 왼쪽이 없음
        if k == 0:
            triangle[j][k] = triangle[j][k] + triangle[j-1][k]
        # 대각선 오른쪽이 없음
        elif j == k:
            triangle[j][k] = triangle[j][k] + triangle[j-1][k-1]
        else:
            triangle[j][k] = triangle[j][k] + max(triangle[j-1][k-1], triangle[j-1][k])

print(max(triangle[n-1]))