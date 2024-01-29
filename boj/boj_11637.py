# Silver 5

import sys

'''
로직

1. 테스트케이스별로 전체 득표 수와 최다 득표 수 계산
2. 
'''

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    
    candidate = []
    
    total, max_cnt = 0, 0
    
    for _ in range(n):
        votes = int(sys.stdin.readline().strip())
        
        candidate.append(votes)
        
        total += votes
    
    # candidate.count(max(candidate)) > ~ 이렇게도 쓸 수 있음    
    for idx in candidate:
        if idx == max(candidate):
            max_cnt += 1
    
    if max_cnt == 1 and max(candidate) > total//2:
        print(f"majority winner {candidate.index(max(candidate))+1}")
    elif max_cnt == 1 and max(candidate) <= total//2:
        print(f"minority winner {candidate.index(max(candidate))+1}")
    else:
        print("no winner")