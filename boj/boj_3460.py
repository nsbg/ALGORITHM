# Bronze 3

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = bin(int(sys.stdin.readline().rstrip()))[2:]

    for i in range(len(n)):
        # [-i-1] 표기로 for문 범위 설정 없이 역순 접근 가능
        if n[-i-1] == '1':
            print(i, end=' ')