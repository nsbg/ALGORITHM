# Level 1

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if (i ** 0.5) % 1 == 0:
            answer -= i
        else:
            answer += i
            
    return answer