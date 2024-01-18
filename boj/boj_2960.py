# Silver 4

import sys

N, K = map(int, sys.stdin.readline().split())

integer_list = [num for num in range(2, N+1)]

remove_check = [0]*(N+1)

remove_check[0] = remove_check[1] = 1

cnt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if remove_check[j] != 1:
            remove_check[j] = 1
            cnt += 1

        if cnt == K and remove_check[j] == 1:
            print(j)
            exit()