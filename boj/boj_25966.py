# Silver 5

import sys

N, M, q = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    col = list(map(int, sys.stdin.readline().split()))

    arr.append(col)

for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] == 0:
        i, j, k = query[1], query[2], query[3]

        arr[i][j] = k
    else:
        i, j = query[1], query[2]

        temp = arr[i]
        
        arr[i] = arr[j]
        arr[j] = temp

for row in arr:
    print(*row, sep=' ')