# Gold 5

import sys
from collections import deque

T = int(input())

for i in range(T):
    isReversed = 0
    isError = 0
    
    cmd = sys.stdin.readline().strip()
    
    n = int(input())
    
    deq = deque(list(sys.stdin.readline().rstrip()[1:-1].split(',')))
    
    if n == 0:
        deq = deque()
    
    for p in cmd:
        if p == 'R':
            if isReversed == 0:
                isReversed = 1
            else:
                isReversed = 0
        elif p == 'D':
            if len(deq) > 0:
                if isReversed == 0: # 짝수 번 뒤집었기 때문에 원본과 동일
                    deq.popleft()
                else:
                    deq.pop()
            else:
                isError = 1
                break
                
    if isReversed == 1:
        deq.reverse()
    
    if isError == 1:
        print("error")
    else:
        print("["+','.join(deq)+"]")