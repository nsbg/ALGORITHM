# Bronze 2

import sys

name = list(sys.stdin.readline().split("-"))

for i in range(len(name)):
    print(name[i][0], end='')