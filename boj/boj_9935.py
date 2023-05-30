# Gold 4

import sys

input_str = sys.stdin.readline().rstrip()
bomb_str = sys.stdin.readline().rstrip()

stack = []

for i in range(len(input_str)):
    stack.append(input_str[i])

    if ''.join(stack[-len(bomb_str):]) == bomb_str:
        for _ in range(len(bomb_str)):
            stack.pop()
      
if len(stack) > 0:
    print(''.join(stack))
else:
    print('FRULA')