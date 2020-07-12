# Silver 5

import sys

numList = list(map(int, sys.stdin.readline().split()))

chk = min(numList)

while True:
    cnt = 0
    
    for i in range(5):
        if chk % numList[i] == 0:
            cnt += 1

    if cnt >= 3:
        print(chk)
        break

    chk += 1