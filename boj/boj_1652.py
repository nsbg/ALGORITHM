# '..'인 케이스만 카운트해주면 됨

import sys

n = int(sys.stdin.readline().rstrip())

check = []

for _ in range(n):
    check.append(list(sys.stdin.readline().rstrip()))

w = 0
h = 0

# 가로 확인
for i in range(n):
    cnt = 0
    for j in range(n):
        if check[i][j] == '.':
            cnt += 1
        else:
            cnt = 0

        if cnt == 2:
            w += 1

# 세로 확인
for i in range(n):
    cnt = 0
    for j in range(n):
        if check[j][i] == '.':
            cnt += 1
        else:
            cnt = 0

        if cnt == 2:
            h += 1

print(w, h)