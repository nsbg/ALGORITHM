# Silver 2
# 정점 a에서 정점 b까지 가는 거리 계산 문제

from collections import deque

n = int(input())

family = [[0]*(n+1) for _ in range(n+1)]
check = [0]*(n+1)

q = deque()

cnt = 0

# 촌수를 계산해야 하는 서로 다른 두 사람
a, b = map(int, input().split())

m = int(input())

for _ in range(m):
    # x: y의 부모 번호
    x, y = map(int, input().split())

    family[x][y] = family[y][x] = 1

q.append(a)

while q:
    pop = q.popleft()

    for i in range(n+1):
        if family[pop][i] == 1 and check[i] == 0:
            check[i] = check[pop] + 1
            q.append(i)

if check[b] != 0:
    print(check[b])
else:
    print(-1)