# Silver 2
# 재귀 알고리즘 다시 공부

import sys

n = int(sys.stdin.readline().rstrip())

def hanoi(num, a, b, c):
    if num == 1:
        print(a, c)
    else:
        hanoi(num-1, a, c, b)
        print(a, c)
        hanoi(num-1, b, a, c)

print(2**n-1)
hanoi(n, 1, 2, 3)