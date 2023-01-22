# Level 2

def solution(A,B):
    answer = 0
    
    for a, b in zip(sorted(A), sorted(B, reverse=True)):
        answer += (a*b)
        
    return answer