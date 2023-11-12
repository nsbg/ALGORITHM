# Silver 3

import sys

def find_mode(number_list):
    max_cnt, mode_num = 0, 0
    
    number_dict = {key: 0 for key in list(set(number_list))}
    
    for number in number_list:
        number_dict[number] += 1
    
    max_mode = max(list(number_dict.values()))
    
    for _, value in number_dict.items():
        if value == max_mode:
            max_cnt += 1

    if max_cnt >= 2:
        mode_num = sorted(number_dict, reverse=True)[1]
    else:
        mode_num = [key for key, value in number_dict.items() if value == max_mode][0]

    return mode_num

N = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list.sort()
print('============')
mean = sum(num_list)/N
median = num_list[int(N/2-0.5)]
mode = find_mode(num_list)
min_max_diff = max(num_list)-min(num_list)

print(mean, median, mode, min_max_diff, sep='\n')