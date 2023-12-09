# Bronze 3

import sys

N = int(sys.stdin.readline().strip())

for i in range(2*N-1):
    if i < N-1:
        print('*'*(i+1)+' '*(2*N-2*(i+1))+'*'*(i+1))
    elif i == N-1:
        print('*'*(2*N))
    else:
        print('*'*(2*N-i-1)+' '*(2*i-2*N+2)+'*'*(2*N-i-1))