# Bronze 2

import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    
    # 내장함수 pow != math.pow
    # pow(a, b, 10): a**b%10 결과 값
    temp = pow(a, b, 10)
    
    if temp == 0:
        print(10)
    else:
        print(temp)