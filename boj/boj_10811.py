# Bronze 2

import sys

N, M = map(int, sys.stdin.readline().split())

basket = [0]+[i for i in range(1, N+1)]

for i in range(M):
    # i번째 바구니부터 j번째 바구니까지의 순서를 역순으로 만듦
    i, j = map(int, sys.stdin.readline().split())

    basket[i:j+1] = basket[i:j+1][::-1]

print(*basket[1:], sep=' ')