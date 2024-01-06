# Silver 5

import sys

# 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, sys.stdin.readline().split())

medals = []

for _ in range(N):
    medal_info = list(map(int, sys.stdin.readline().split()))
    
    medals.append(medal_info)

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if medals[i][0] == K:
        rank = i

for j in range(N):
    if medals[j][1:] == medals[rank][1:]:
        print(j+1)
        break