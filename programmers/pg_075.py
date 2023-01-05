# Level 2

def solution(s):
    s = list(s)
    
    stack = []
    
    if s[0] == ')':
        return False
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    
    if stack == []:
        return True
    else:
        return False