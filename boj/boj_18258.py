# Silver 4

import sys

from collections import deque

deq = deque()

N = int(sys.stdin.readline().rstrip())

while N > 0:
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push':
        deq.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deq))
    elif cmd[0] == 'empty':
        if len(deq) > 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)
    
    N -= 1