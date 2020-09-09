# Bronze 1

import sys

square = [[int(row) for row in sys.stdin.readline().split()] for col in range(4)]

chkSum = []

for i in range(0, 4):
    row, col = 0, 0

    row = sum(square[i])
    chkSum.append(row)

    for j in range(0, 4):
        col += square[j][i]

    chkSum.append(col)

if len(set(chkSum)) == 1:
    print("magic")
else:
    print("not magic")