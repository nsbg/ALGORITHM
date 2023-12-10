# Silver 5

import sys

M = int(sys.stdin.readline().strip())

S = []

for _ in range(M):
    operation = list(sys.stdin.readline().split())
    
    if operation[0] == 'add':
        if int(operation[1]) not in S:
            S.append(int(operation[1]))
    elif operation[0] == 'remove':
        if int(operation[1]) in S:
            S.remove(int(operation[1]))
    elif operation[0] == 'toggle':
        if int(operation[1]) in S:
            S.remove(int(operation[1]))
        else:
            S.append(int(operation[1]))
    elif operation[0] == 'all':
        S = [i for i in range(1, 21)]
    elif operation[0] == 'empty':
        S = []
    elif operation[0] == 'check':
        if int(operation[1]) in S:
            print(1)
        else:
            print(0)