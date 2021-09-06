# Silver 1

import sys
from collections import deque

M, N, H = map(int, input().split())

farm = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if farm[i][j][k] == 1:
                q.append((i, j, k))

def BFS():
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dz = [1, -1, 0, 0, 0, 0]

    while q:
        tomato_z, tomato_x, tomato_y = q.popleft()

        for i in range(6):
            check_x = tomato_x+dx[i]
            check_y = tomato_y+dy[i]
            check_z = tomato_z+dz[i]

            if 0<= check_x < N and 0<= check_y < M and 0<= check_z < H:
                if farm[check_z][check_x][check_y] == 0:
                    farm[check_z][check_x][check_y] = farm[tomato_z][tomato_x][tomato_y]+1
                    q.append((check_z, check_x, check_y))

BFS()

isAvailable = True
day = 0

for i in farm:
    for j in i:
        for k in j:
            if k == 0:
                isAvailable = False
            
            day = max(day, k)

if isAvailable == False:
    print(-1)
else:
    print(day-1)