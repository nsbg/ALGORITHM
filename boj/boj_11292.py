# Silver 5

import sys

while True:
    T = int(sys.stdin.readline().strip())
    
    info = []
    result = []
    
    if T == 0:
        break

    for i in range(T):
        name, height = sys.stdin.readline().split()
        
        height = float(height)
        
        info.append([name, height])
            
    max_height = max(item[1] for item in info)
    
    for j in info:
        if j[1] == max_height:
            result.append(j[0])
    
    print(*result)