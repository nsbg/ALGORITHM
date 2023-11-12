# Silver 3

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    importance = deque(sys.stdin.readline().split())
    doc = [i for i in range(N)]

    printer = []

    while len(importance) != 0:
        if importance[0] == max(importance):
            printer.append(doc.pop(0))
            importance.popleft()
        else:
            importance.append(importance.popleft())
            doc.append(doc.pop(0))

    print(printer.index(M)+1)