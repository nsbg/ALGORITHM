# Silver 5

import sys

real = int(input())

n = list(map(int, sys.stdin.readline().split()))

# 그냥 최소공배수를 찾으면 틀림 -> 4, 2 최소공배수는 4이지만 예제 답은 8
print(min(n)*max(n))