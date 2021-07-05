# Silver 4

import sys

n = int(input())

for _ in range(n):
    stack = []
    check = 0
    
    parenthesis = sys.stdin.readline().rstrip()

    for p in parenthesis:
        if p=="(":
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                # 이미 쌍이 다 만들어졌는데 ) 한 쪽만 들어온 상태
                print("NO")
                check = 1
                break
    
    if len(stack) != 0 and check == 0:
        print("NO")
    elif len(stack) == 0 and check == 0:
        print("YES")