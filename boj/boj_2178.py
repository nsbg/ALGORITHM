# Silver 1

from collections import deque

n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

visited[0][0] = True

# start_x, start_y : 좌표 값
def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()

        # 상하좌우 체크
        for i in range(4):
            check_x = x+dx[i]
            check_y = y+dy[i]

            if 0 <= check_x < n and 0 <= check_y < m:
                if visited[check_x][check_y] == False and maze[check_x][check_y] == 1:
                    maze[check_x][check_y] = maze[x][y]+1
                    q.append((check_x, check_y))
                    visited[check_x][check_y] = True

    return maze[n-1][m-1]

print(bfs(0, 0))