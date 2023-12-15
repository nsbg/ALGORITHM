# Silver 5

# 슈트라센 알고리즘

import sys

A = []
B = []

N, MA = map(int, sys.stdin.readline().split())

# 행렬 A
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

MB, K = map(int, sys.stdin.readline().split())

# 행렬 B
for _ in range(MB):
    B.append(list(map(int, sys.stdin.readline().split())))

# N행 K열의 2차원 배열 초기화
result = [[0 for _ in range(K)] for _ in range(N)]

# 행렬 곱 수행
for row in range(N):
    for col in range(K):
        for temp_row in range(MA):
            result[row][col] += (A[row][temp_row]*B[temp_row][col])

# 결과 행렬 요소 출력
for elements in result:
    print(*elements, sep=' ')