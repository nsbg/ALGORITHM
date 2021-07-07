# Bronze 1

import sys

n = int(input())

for _ in range(n):
    p = int(input())

    playerList = {}

    for _ in range(p):
        c, playerName = sys.stdin.readline().split()
        playerList[playerName] = int(c)

    maxValue = max(playerList.values())

    for k, v in playerList.items():
        if v == maxValue:
            print(k)