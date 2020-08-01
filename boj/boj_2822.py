# Silver 5

import sys

idxChk = []

score = [int(sys.stdin.readline().rstrip()) for i in range(8)]

highScore = sorted(score, reverse=True)[0:5]

print(sum(highScore))

for i in highScore:
    idxChk.append(score.index(i)+1)
    idxChk = sorted(idxChk)

for j in idxChk:
    print(j, end=' ')