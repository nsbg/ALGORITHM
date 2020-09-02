# Silver 5

import sys


def factorial(num):
    f = [0]*30

    f[0] = 1
    f[1] = 1

    for i in range(2, 30):
        f[i] = i * f[i-1]

    return f[num]


t = int(input())

for _ in range(t):
    res = 0

    n, m = map(int, sys.stdin.readline().split())

    k = m-n

    numerator = factorial(m)                    # 분자
    denominator = factorial(k) * factorial(n)   # 분모

    res = numerator//denominator

    print(res)