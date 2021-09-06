# Silver 1

from collections import deque

import sys

q = deque()

M, N = map(int, input().split())

farm = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 익은 곳에서부터 퍼져나가기 때문에 익은 토마토 위치를 저장해줘야 함
for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            q.append((i, j))

# 이미 큐에 익은 토마토 위치가 저장되어 있어서 시작점을 큐에 따로 추가하지 않아도 됨
def BFS():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        tomato_x, tomato_y = q.popleft()

        for i in range(4):
            check_x = tomato_x+dx[i]
            check_y = tomato_y+dy[i]

            if 0<= check_x < N and 0<= check_y < M:
                # 안 익은 토마토일 때
                if farm[check_x][check_y] == 0:
                    # 며칠째에 익는지 바로 계산
                    farm[check_x][check_y] = farm[tomato_x][tomato_y]+1
                    q.append((check_x, check_y))

isAvailable = True
day = 0

BFS()

for f in farm:
    for t in f:
        if t == 0:
            isAvailable = False
        
        day = max(day, t)

if isAvailable == False:
    print(-1)
else:
    print(day-1)