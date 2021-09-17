# Gold 4

import sys

sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())

# 각 노드의 초기 부모 노드는 자기 자신
parent = [i for i in range(n+1)]

def union(x, y):
    x = find(x)
    y = find(y)

    # 더 작은 노드가 부모
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(currentNode):
    if parent[currentNode] == currentNode:
        return currentNode
    else:
        parent[currentNode] = find(parent[currentNode])
        
    return parent[currentNode]

for _ in range(m):
    check, a, b = map(int, input().split())

    if check:
        # 부모 노드 같은지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)