# Silver 5

import sys

# 대회 참가 학생 수
N = int(input())

student_result = []

country_count = []

for _ in range(N):
    # 소속 국가 번호, 학생 번호, 성적
    student_info = list(map(int, sys.stdin.readline().split()))
        
    student_result.append(student_info)
    
student_result.sort(key=lambda x: x[2], reverse=True)

for i in range(0, len(student_result)):
    if country_count.count(student_result[i][0]) < 2:
        print(student_result[i][0], student_result[i][1])
        country_count.append(student_result[i][0])
    
    if len(country_count) == 3:
        break