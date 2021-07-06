# Bronze 2

import sys

t = int(input())

for i in range(t):
    mars = list(map(str, sys.stdin.readline().split()))
    answer = float(mars[0])

    for m in range(1, len(mars)):
        if mars[m] == "@":
            answer *= 3
        elif mars[m] == "%":
            answer += 5
        else:
            answer -= 7
    
    print('%.2f' % answer)