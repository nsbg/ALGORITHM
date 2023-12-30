# Bronze 2

# 삼성 SW 역량 테스트, 736ms

import sys

from math import ceil

N = int(sys.stdin.readline().strip())

answer = 0

exmination_site = list(map(int, sys.stdin.readline().split()))

# B: 한 시험장에서 총감독관이 감시할 수 있는 응시자의 수
# C: 한 시험장에서 부감독관이 감시할 수 있는 응시자의 수
B, C = map(int, sys.stdin.readline().split())

for i in exmination_site:
    if i-B <= 0:
        answer += 1
    else:
        temp = i

        temp -= B

        if temp%C != 0:
            answer += (temp//C)+1
        else:
            answer += (temp//C)

        answer += 1

print(answer)