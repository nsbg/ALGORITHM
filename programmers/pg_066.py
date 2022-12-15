# Level 1

def solution(k, score):
    answer = []
    honor = []
    
    for i in score:
        honor.append(i)
        
        if len(honor) > k:
            honor = sorted(honor)[1:]
        
        answer.append(min(honor))
        
    return answer