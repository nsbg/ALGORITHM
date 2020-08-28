# Bronze 3
# 1번 컵과 공이 같이 움직인다고 생각, 1번 컵의 위치 출력해주기

import sys

m = int(input())

temp = 0

cup = [0, 1, 2, 3]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    temp = cup[x]
    cup[x] = cup[y]
    cup[y] = temp

print(cup.index(1))