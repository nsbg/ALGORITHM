# Silver 3

import sys

n = int(input())
m = int(input())

connected = [[0]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)

cnt = 0

for _ in range(m):
    c1, c2 = map(int, input().split())

    connected[c1][c2] = connected[c2][c1] = 1

def dfs(v):
    global cnt

    visited[v] = True

    for i in range(n+1):
        if connected[v][i] == 1 and visited[i] == 0 :
                connected[v][i] = connected[i][v] = 0
                visited[i] = 1
                dfs(i)
                cnt += 1

    return cnt

print(dfs(1))