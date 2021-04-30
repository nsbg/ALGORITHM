# Silver 3

import sys

n, p = map(int, input().split())
w, l, g = map(int, input().split())

findedPlayer = dict()

score = 0
win = False

playerScore = []

for _ in range(p):
    name, wl = map(str, sys.stdin.readline().split())
    findedPlayer[name] = wl

for _ in range(n):
    playerScore.append(sys.stdin.readline().rstrip())

for p in playerScore:
    if p not in findedPlayer.keys():
        score -= l
    else:
        if findedPlayer[p] == "W":
            score += w
        elif findedPlayer[p] == "L":
            score -= l

    if score < 0:
        score = 0

    if score >= g:
        win = True
        break

if not win:
    print("I AM IRONMAN!!")
else:
    print("I AM NOT IRONMAN!!")