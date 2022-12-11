def solution(s):
    answer = 0
    
    x_cnt = 0
    not_x_cnt = 0

    x = ''
    
    for alphabet in s:
        if x == '':
            x = alphabet
        
        if alphabet == x:
            x_cnt += 1
        else:
            not_x_cnt += 1
        
        if x_cnt == not_x_cnt:
            answer += 1
            
            x = ''
            x_cnt = 0
            not_x_cnt = 0
        
    if x:
        answer += 1
    
    return answer