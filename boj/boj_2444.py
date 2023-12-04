# Bronze 3

import sys

N = int(sys.stdin.readline().strip())

for i in range(0, 2*N-1):
    if i < N-1:
        print(' '*(N-i-1)+'*'*(2*i+1))
    elif i == N-1:
        print('*'*(2*N-1))
    else:
        print(' '*(i-N+1)+'*'*(4*N-2*i-3))