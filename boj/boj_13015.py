# Silver 4

import sys

N = int(input())

for i in range(0, 2*N-1):
    if i == 0 or i == 2*N-2:
        print('*'*N+' '*(2*N-3)+'*'*N)
    elif i < N-1:
        print(' '*i+'*'+' '*(N-2)+'*'+' '*(2*N-2*i-3)+'*'+' '*(N-2)+'*')
    elif i == N-1:
        print(' '*i+'*'+' '*(N-2)+'*'+' '*(N-2)+'*')
    else:
        print(' '*(2*N-i-2)+'*'+' '*(N-2)+'*'+' '*(2*i-2*N+1)+'*'+' '*(N-2)+'*')