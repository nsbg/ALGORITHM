# Silver 4

import sys

N = int(input())

q = []

while N > 0:
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) > 0:
            print(q.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
    
    N -= 1