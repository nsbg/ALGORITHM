# Bronze 1

import sys

S = list(input())

stack = []

for s in S:
    stack.append(s)
    
while len(S) > 0:
    if S.pop() != stack.pop(0):
        print(0)
        sys.exit(0)

print(1)