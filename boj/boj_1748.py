# Silver 4

import sys

N = sys.stdin.readline().strip()

answer = 0

# (N-1)자릿수까지 다 더하기
for i in range(1, len(N)):
    answer += 9*10**(i-1)*i

answer += (int(N)-10**(len(N)-1)+1)*len(N)

print(answer)