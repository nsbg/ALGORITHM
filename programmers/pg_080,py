# Level 2

def solution(s):
    zero_count, transform_count = 0, 0
    
    x = s
    
    while len(s) > 1:
        zero_count += x.count('0')
        
        x = x.replace('0', '')
        
        x = bin(len(x))[2:]
        s = x
        
        transform_count += 1
    
    answer = [transform_count, zero_count]
    
    return answer