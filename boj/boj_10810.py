# Bronze 3

import sys

N, M = map(int, sys.stdin.readline().split())

ball = [0]*(N+1)

for idx1 in range(M):
    # i번 바구니부터 j번 바구니까지 k번 공을 넣음
    i, j, k = map(int, sys.stdin.readline().split())
    
    for idx2 in range(i, j+1):
        ball[idx2] = k

print(*ball[1:], sep=' ')