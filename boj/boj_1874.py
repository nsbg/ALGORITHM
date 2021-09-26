# Silver 3

import sys

N = int(sys.stdin.readline().rstrip())

stack = []
result = []

idx = 1

flag = True

for i in range(N):
    num = int(sys.stdin.readline().rstrip())

    while idx <= num:
        result.append("+")
        stack.append(idx)

        idx += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False

if flag == False:
    print("NO")
else:
    for r in result:
        print(r)