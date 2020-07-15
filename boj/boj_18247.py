# Bronze 3

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    # n : 열, m : 한 열에 속한 좌석 개수
    n, m = map(int, sys.stdin.readline().split())

    if n < 12 or m < 4:
        print('-1')
    else:
        print(m*11 + 4)