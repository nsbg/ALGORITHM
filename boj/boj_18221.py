# Silver 5

import sys

'''
로직

1. 성규와 교수님 위치 확인
    - 같은 행에 있는 경우
    - 같은 열에 있는 경우
    - 행, 열이 모두 다른 경우
2. 각 경우에 대해
    - 거리가 5 미만이면 0
    - 거리가 5 이상이고 그 사이에 성규 외의 학생이 세 명 미만일 때 0
    - 거리가 5 이상이고 그 사이에 성규 외의 학생이 세 명 이상일 때 1
'''

N = int(input())

desk = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

flag = 0 # 성규, 교수님의 같은 행 또는 열에 있는지 확인하기 위한 역할

sk, prof = [], []

for i, value in enumerate(desk):
    for j, pos in enumerate(desk[i]):
        if pos == 2:
            sk.extend([i, j])
        
        if pos == 5:
            prof.extend([i, j])

if sk[0] == prof[0]:
    flag = 1
elif sk[1] == prof[1]:
    flag = 2
    
d = (sk[0]-prof[0])**2+(sk[1]-prof[1])**2

cnt = 0

start_row, end_row = min(sk[0], prof[0]), max(sk[0], prof[0])
start_col, end_col = min(sk[1], prof[1]), max(sk[1], prof[1])
    
if d < 25:
    print(0)
elif d >= 25 and flag == 0:    
    for i in range(start_row, end_row+1):
        for j in desk[i][start_col:end_col+1]:
            if j == 1:
                cnt += 1
    
    if cnt >= 3:
        print(1)
    else:
        print(0)          
elif d >= 25 and flag == 1: # 같은 행
    for i in desk[start_row][start_col:end_col+1]:
        if i == 1:
            cnt += 1
    
    if cnt >= 3:
        print(1)
    else:
        print(0)
elif d >= 25 and flag == 2: # 같은 열
    for i in range(start_row, end_row+1):
        if desk[i][sk[1]] == 1:
            cnt += 1
        
    if cnt >= 3:
        print(1)
    else:
        print(0)