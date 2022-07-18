# Bronze 2
# 시간이 비효율적인 코드

import sys

N = int(sys.stdin.readline().rstrip())

result = 0

for i in range(1, N+1):
    tmp = list(str(i))
    calc = i+sum(map(int, tmp))
    
    if calc == N:
        result = ''.join(tmp)
        break

print(result)