# Level 1

def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
    
    fruit = []
    
    for i in score:
        fruit.append(i)
        
        if len(fruit) == m:
            answer += min(fruit)*m
            fruit = []
            
    return answer