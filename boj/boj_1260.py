# Silver 2

import sys

from collections import deque

n, m, v = map(int, input().split())

# 인덱스 헷갈리지 않게 하려고 (n+1)*(n+1) 크기의 인접행렬 생성
adjMatrix = [[0]*(n+1) for _ in range(n+1)]

# 방문 체크용 배열 생성
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    # 양방향 연결을 의미
    adjMatrix[a][b] = adjMatrix[b][a] = 1

def dfs(v):
    visited[v] = 1

    print(v, end=' ')

    for j in range(1, n+1):
        # 출발점 v의 인접노드이지만 방문한 적이 없는 노드
        if adjMatrix[v][j] == 1 and visited[j] == 0 :
            dfs(j)


def bfs(V):
    bfsVisited = [V]

    q = deque() # 큐 생성
    q.append(V) # 방문 처리한 노드는 큐에 삽입

    while q:
        pop = q.popleft()
        print(pop, end=' ')

        # 방문 처리 되지 않은 인접 노드 모두 큐에 삽입
        for k in range(len(adjMatrix[V])):
            if adjMatrix[pop][k] == 1 and (k not in bfsVisited):
                q.append(k)
                bfsVisited.append(k)

dfs(v)
print()
bfs(v)

