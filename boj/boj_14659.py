# Bronze 2
# n명의 활잡이 중에서 적을 가장 많이 처치한 활잡이가 몇 명을 처치했는지 출력

# PyPy로 내니까 통과는 됐는데 그리디 이용하면 파이썬으로도 통과 가능

import sys

n = int(sys.stdin.readline().rstrip())

height = list(map(int, sys.stdin.readline().split()))

bestArcher = 0

for i in range(len(height)):
    cnt = 0

    for j in range(i+1, len(height)):
        if height[i] > height[j]:
            cnt += 1
        else:
            break

    if cnt > bestArcher:
        bestArcher = cnt
    else:
        bestArcher

print(bestArcher)