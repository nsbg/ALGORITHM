# Silver 3
# 15649번과 차이점 : 수열은 오름차순이어야 함
 
import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

def DFS(j):
    if len(arr) == M:
        print(*arr, sep=' ')
        return

    for i in range(j, N+1):
        if i not in arr:
            arr.append(i)
            DFS(i+1)
            arr.pop()
    
DFS(1)