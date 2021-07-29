# Silver 1

import sys

# 단지 내 집 수
cnt = 0

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if matrix[x][y] == 1:
        global cnt # 전역변수 cnt_part를 함수 안에서 쓰겠다고 선언

        cnt += 1

        matrix[x][y] = 0

        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)

        return True
    
    return False

n = int(input())

matrix = []
result = []

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

for j in range(n):
    for k in range(n):
        if dfs(j, k) == True:
            result.append(cnt)
            cnt = 0

print(len(result))

for r in sorted(result):
    print(r)