# Silver 1

import sys
from collections import deque

N, K = map(int, input().split())

cnt = 0

visited = [0]*100001

def BFS():
    q = deque()
    q.append(N)
    
    while q:
        cur = q.popleft()
        
        move = [cur-1, cur+1, cur*2]

        if cur == K:
            print(visited[cur])
            break
        
        for m in move:
            if 0<= m <= 100000 and visited[m] == 0:
                visited[m] = visited[cur]+1
                q.append(m)

BFS()