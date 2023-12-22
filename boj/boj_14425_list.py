# Silver 4

import sys

N, M = map(int, sys.stdin.readline().split())

str_in_S = []
check_list = []

cnt = 0

for _ in range(N):
    str_in_S.append(sys.stdin.readline().strip())

# 입력 M은 중복이 있을 수 있음
for _ in range(M):
    check_list.append(sys.stdin.readline().strip())

for element in check_list:
    if element in str_in_S:
        cnt += 1

print(cnt)