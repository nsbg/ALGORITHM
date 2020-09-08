# Silver 4
# 변수 위치 중요

import sys

n = int(input())

firstNum = sorted(list(map(int, sys.stdin.readline().split())))

m = int(input())

secondNum = list(map(int, sys.stdin.readline().split()))

for i in secondNum:
    res = 0

    low = 0
    high = len(firstNum) - 1

    while low <= high:
        mid = (low+high)//2

        if i == firstNum[mid]:
            res = 1
            break
        elif i < firstNum[mid]:
            high = mid-1
        else:
            low = mid+1

    print(res)