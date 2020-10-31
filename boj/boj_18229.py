# Bronze 1

import sys

n, m, k = map(int, sys.stdin.readline().split())

p = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

total = [0] * n

# 손 뻗은 횟수
for cnt in range(m):
    # 몇번째 사람인지 확인
    for person in range(n):
        total[person] += p[person][cnt]

        if total[person] >= k:
            print(person+1, cnt+1)
            exit()