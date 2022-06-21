# Silver 4

import sys

from collections import deque

N = int(sys.stdin.readline().rstrip())

deq = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_front":
        deq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front":
        if len(deq) > 0:
            print(deq.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if len(deq) > 0:
            print(deq.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if len(deq) > 0:
            print(deq[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(deq) > 0:
            print(deq[-1])
        else:
            print(-1)