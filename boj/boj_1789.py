# Silver 5

import sys

S = int(sys.stdin.readline().strip())

num_list = [0]*100001

num_list[1] = 1

for i in range(2, 100001):
    num_list[i] = num_list[i-1]+i

for j in range(1, len(num_list)):
    if num_list[j] == S:
        print(j)
        break
    elif num_list[j-1] < S and num_list[j] > S:
        print(j-1)
        break