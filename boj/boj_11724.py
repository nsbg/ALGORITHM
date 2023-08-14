# Silver 2

import sys

sys.setrecursionlimit(10**6) # DFS를 위한 재귀 제한 값 설정

from collections import deque

def DFS(graph, node, visited):
    visited[node] = True # 노드 방문 처리
    
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i, visited)

def BFS(graph, node, visited):
    queue = deque([node])
    
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
N, M = map(int, sys.stdin.readline().split())

visited = [False]*(N+1)

component_cnt = 0

graph = [[] for _ in range(N+1)]

# 그래프 생성
for _ in range(M):
    '''
        [
            [],
            [2, 5],
            [1, 5],
            [4],
            [3, 6],
            [1, 2],
            [4]
        ]
    '''
    u, v = map(int, sys.stdin.readline().split())
    
    graph[u].append(v) # u번 노드와 연결된 노드가 v
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        DFS(graph, i, visited)
        # BFS(graph, i, visited)
          
        component_cnt += 1

print(component_cnt)