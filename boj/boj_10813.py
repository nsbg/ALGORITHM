# Bronze 2

import sys

import sys

N, M = map(int, sys.stdin.readline().split())

ball = [0]+[i for i in range(1, N+1)]

tmp = 0

for i in range(M):
    i, j = map(int, sys.stdin.readline().split())
    
    tmp = ball[i]
    
    ball[i] = ball[j]
    ball[j] = tmp

print(*ball[1:], sep=' ')