# Silver 2

import sys
from collections import deque

sys.setrecursionlimit(10**8)

dx=[1,-1,0,0]
dy=[0,0,-1,1]

# DFS → 스택이나 재귀
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if field[x][y] == 1:
        field[x][y] = 0

        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x-1, y)
        dfs(x+1, y)

        return True
    
    return False

# BFS
def bfs(x, y):
    q = deque()

    # 시작 위치 넣어줌
    q.append((x, y))

    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < N and 0 <= yy < M and field[nx][ny] == 1:
                # 방문한 곳은 0으로 바꿔주기
                field[xx][yy] = 0
                q.append((x, y))


t = int(input())

for _ in range(t):
    M, N, K = map(int, input().split())
    
    field = [[0]*M for _ in range(N)]

    # BFS 방문체크용 배열
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        m, n = map(int, input().split())

        field[n][m] = 1
    
    worm = 0
    
    for i in range(N):
        for j in range(M):
            # 배추가 있는 지역의 인접 지역까지 모두 탐색을 끝낸 경우
            if dfs(i, j) == True:
                worm += 1
    
    print(worm)