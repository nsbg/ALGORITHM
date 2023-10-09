# Bronze 1

while True:
    N = input()
    
    flag = 0
    
    if N == '0':
        break
    
    stack = [num for num in N]
    
    while len(stack) > 1:
        if stack.pop() != stack.pop(0):
            flag = 1
            break
        
    if flag == 1:
        print('no')
    else:
        print('yes')