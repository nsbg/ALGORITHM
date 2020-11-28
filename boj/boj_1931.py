# Silver 2

import sys

n = int(input())

cnt = 0

# 끝나는 시간
end = 0

conference = []

for i in range(n):
    c = list(map(int, sys.stdin.readline().split()))

    conference.append(c)

# s : 회의 시작 시간, e : 회의 끝나는 시간
for s, e in sorted(conference):
    if s >= end:
        end = e
        cnt += 1
    elif e <= end:
        end = e

print(cnt)