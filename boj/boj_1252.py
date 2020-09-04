# Bronze 1

import sys

a, b = sys.stdin.readline().split()

# int('바꿀 대상', 2/8/16) : 10진수로 변환
a = int(a, 2)
b = int(b, 2)

if a == 0 and b == 0:
    print(0)
else:
    print(bin(a+b)[2:])