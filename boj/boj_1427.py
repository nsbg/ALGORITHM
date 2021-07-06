# Silver 5

import sys

n = sorted(list(map(int, sys.stdin.readline().rstrip())), reverse=True)

for i in range(len(n)):
    print(n[i], end='')

