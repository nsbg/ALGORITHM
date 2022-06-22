# Silver 5
# 원형 큐, 일반 큐 둘다 가능

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, N+1)])

josephus = []

while True:
    if len(josephus) == N:
        break

    for i in range(K-1):
        deq.append(deq.popleft())
    
    josephus.append(deq.popleft())

print("<"+', '.join(map(str, josephus))+">")