# Level 1

def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
    
    high_prize = correct+lottos.count(0)
    low_prize = correct
    
    if low_prize == 0:
        low_prize = 1
        
    if correct == 0 and lottos.count(0) == 0:
        answer = [6, 6]
    else:
        answer = [7-high_prize, 7-low_prize]
    
    return answer