# Silver 4

import sys

def customize_round(num):
    round_result = 0
    
    integer_part = int(num)
    point_part = num-integer_part
    
    if 1-point_part > 0.5:
        point_part = 0
    else:
        point_part = 1
        
    round_result = integer_part+point_part
    
    return round_result

n = int(sys.stdin.readline().rstrip())

if n == 0:
    print(0)
    exit()
    
except_num = customize_round(n*0.15)

comments = []

for i in range(n):
    comments.append(int(sys.stdin.readline().rstrip()))

comments.sort()

filtered_comments = comments[except_num:n-except_num]

print(customize_round(sum(filtered_comments)/len(filtered_comments)))