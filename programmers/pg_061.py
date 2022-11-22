# Level 2

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    
    total = (q1_sum+q2_sum)//2

    cnt = 0
    
    if max(q1) > total or max(q2) > total:
        return -1
    
    while q1 and q2:
        if q1_sum > q2_sum:
            popped = q1.popleft()
            
            q2.append(popped)
            
            q1_sum -= popped
            q2_sum += popped
            
            cnt += 1
        elif q1_sum < q2_sum:
            popped = q2.popleft()
            
            q1.append(popped)
            
            q1_sum += popped
            q2_sum -= popped
            
            cnt += 1
        else:
            break
        
        if cnt == len(q1)*4:
            cnt = -1
            break
            
    return cnt