# Level 2

def solution(s):
    stack = [s[0]]
    
    for i in s[1:]:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    return 1 if len(stack) == 0 else 0