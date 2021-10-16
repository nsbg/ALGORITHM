# Silver 4

import sys

while True:
    words = sys.stdin.readline().rstrip()

    if words == ".":
        break

    stack = []

    for w in words:
        if w == "(" or w == "[":
            stack.append(w)
        elif w == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(w)
                break
    
    if len(stack) !=0 :
        print("no")
    else:
        print("yes")