# Silver 3

import sys

n, m = map(int, input().split())

tree = sorted(list(map(int, sys.stdin.readline().split())))

start = 0
end = max(tree)

while start <= end:
    mid = (start+end)//2

    ans = 0
    ans = sum([t-mid if t-mid>=0 else 0 for t in tree])

    if ans >= m:
        start = mid+1
    else:
        end = mid-1

print(end)