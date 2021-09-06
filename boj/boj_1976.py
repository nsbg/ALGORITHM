# Gold 4
# 주어진 도시들이 모두 같은 집합에 속하는지 확인하는 문제(최종 집합이 1개여야 함)
import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

cities = [i for i in range(n+1)]

# 부모 노드 찾기
def find(currentCity):
    if currentCity == cities[currentCity]:
        return currentCity
    
    cities[currentCity] = find(cities[currentCity])
    
    return cities[currentCity]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        cities[y] = x
    else:
        cities[x] = y

# for i in range(1, n+1):
#     connect = list(map(int, sys.stdin.readline().split()))

#     for j in range(1, n):
#         if connect[j] == 1:
#             union(i, j)

for i in range(1, n+1):
    connect = list(map(int, sys.stdin.readline().split()))

    for j in range(1, n+1):
        if connect[j-1] == 1:
            union(i, j)

plan = list(map(int, sys.stdin.readline().split()))  
result = set([find(i) for i in plan])

# print(result)
if len(result) != 1:
    print("NO")
else:
    print("YES")