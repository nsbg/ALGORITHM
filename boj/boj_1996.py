# Bronze 1

import sys

n = int(input())

numList = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

map = numList

# 한 점과 주변 8칸 좌표값 차이 x, y로 나눠서 저장
chk_x = [-1, -1, -1, 0, 0, 1, 1, 1]
chk_y = [1, 0, -1, 1, -1, 1, 0, -1]


for i in range(0, n):
    for j in range(0, n):
        if numList[i][j] != '.':
            map[i][j] = '*'
        # 지뢰가 아닐 때
        else:
            map[i][j] = '0'


            # for k in range(0, 8):
            #     x = i + chk_x[k]
            #     y = j + chk_y[k]
            #
            #     if x < 0 or y < 0:
            #         continue

print(map)

# for M in map:
#     print(*M, sep='')