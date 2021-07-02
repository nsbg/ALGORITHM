# Level 2

def solution(clothes):
    answer = 1
    spy = {}
    
    for c in clothes:
        if c[1] in spy:
            spy[c[1]] += 1
        else:
            spy[c[1]] = 1
    
    for s in spy.values():
        answer *= (s+1)
    
    return answer-1