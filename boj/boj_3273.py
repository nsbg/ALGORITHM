# Silver 4
# 이분 탐색

import sys

n = int(input())

numList = sorted(map(int, sys.stdin.readline().split()))

x = int(input())

start = 0
end = n-1

cnt = 0

while start != end:
    res = numList[start] + numList[end]

    if res == x:
        cnt += 1
        start += 1
    elif res < x:
        start += 1
    else:
        end -= 1

print(cnt)