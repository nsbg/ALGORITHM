# Bronze 3

import sys

N = int(sys.stdin.readline().strip())

for i in range(0, 2*N-1):
    if i <= N-1:
        print(' '*i+'*'*(2*N-2*i-1))
    else:
        print(' '*(2*N-i-2)+'*'*(2*i-2*N+3))