# Silver 4

import sys

n = int(input())
num = sorted(map(int, sys.stdin.readline().split()))

# num = [-10, -10, 2, 3, 3, 6, 7, 10, 10, 10]
m = int(input())
checkNum = list(map(int, sys.stdin.readline().split()))

numDict = {}

for n in num:
    try:
        numDict[n] += 1
    # 맨처음 n이 나오면 키가 없기 때문에 에러 띄우는 게 아니라 예외처리
    except:
        numDict[n] = 1

for c in checkNum:
    if c in numDict:
        sys.stdout.write(str(numDict[c])+' ')
    else:
        sys.stdout.write("0 ")