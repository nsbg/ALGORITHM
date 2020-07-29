# Silver 5

import sys

def gcd(num1, num2):
    if num1 < num2:
        tmp = num1
        num1 = num2
        num2 = tmp

    while num2 != 0:
        n = num1 % num2
        num1 = num2
        num2 = n

    return num1


# 사과, 바나나 순
a, b = map(int, sys.stdin.readline().split())

chk_gcd = gcd(a, b)

for i in range(1, chk_gcd+1):
    if chk_gcd % i == 0:
        print(i, a//i, b//i, sep=' ')
    else:
        continue