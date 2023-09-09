# Level 2

import math

def solution(progresses, speeds):
    answer = []
    
    complete_days = []
    
    for i in range(len(progresses)):
        complete_days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    cnt = 1
    
    # complete_days = [7, 3, 9], [5, 10, 1, 1, 20, 1]
    standard = complete_days[0]
    
    for day in range(1, len(complete_days)):
        if standard >= complete_days[day]:
            cnt += 1
        else:
            answer.append(cnt)
            
            cnt = 1
            
            standard = complete_days[day]

    answer.append(cnt)
        
    return answer