# Silver 5

import sys

K = int(sys.stdin.readline().strip())

for i in range(K):
    gap  = []
    
    class_info = list(map(int, sys.stdin.readline().split()))
    class_info = sorted(class_info[1:], reverse=True)

    for j in range(len(class_info)-1):
        gap.append(class_info[j]-class_info[j+1])

    print(f"Class {i+1}")
    print(f"Max {max(class_info)}, Min {min(class_info)}, Largest gap {max(gap)}")