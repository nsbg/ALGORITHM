# Silver 5

import sys

N = sys.stdin.readline().strip()

# 숫자가 나오는 횟수를 체크하기 위한 리스트
number_count = [0]*10
            
for i in N:
    if i == '6' or i == '9':
        if number_count[6] <= number_count[9]:
            number_count[6] += 1
        else:
            number_count[9] += 1
    else:
        number_count[int(i)] += 1

print(max(number_count))