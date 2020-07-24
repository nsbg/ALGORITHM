# Bronze 2

import sys

n = int(sys.stdin.readline().rstrip())

radius = [9, 36, 81, 144, 225]

for _ in range(n):
    player = list(map(float, sys.stdin.readline().split()))

    firstPlayerPoint = 0
    secondPlayerPoint = 0

    for i in range(0, 6, 2):
        firstPlayerRadius = player[i]**2 + player[i+1]**2

        for f, d1 in enumerate(radius):
            if firstPlayerRadius <= d1:
                firstPlayerPoint += 100 - (20*f)
                break

    for j in range(6, 11, 2):
        secondPlayerRadius = player[j]**2 + player[j+1]**2

        for s, d2 in enumerate(radius):
            if secondPlayerRadius <= d2:
                secondPlayerPoint += 100 - (20*s)
                break

    if firstPlayerPoint == secondPlayerPoint:
        print("SCORE:", firstPlayerPoint, "to", str(secondPlayerPoint)+", TIE.")
    elif firstPlayerPoint > secondPlayerPoint:
        print("SCORE:", firstPlayerPoint, "to", str(secondPlayerPoint)+", PLAYER 1 WINS.")
    else:
        print("SCORE:", firstPlayerPoint, "to", str(secondPlayerPoint)+", PLAYER 2 WINS.")