# Gold 4

import sys

N = int(input())

A = list(map(int ,sys.stdin.readline().split()))

NGE = [-1]*N

# index 보관용
stack = [0]

for i in range(1, N):
    # 1. while 없으면 현재 인덱스보다 하나 뒤에 있는 것만 확인함
    # 2. 예제 입력 1의 5 같은 경우 2만 보고 끝나면 안됨
    while stack and A[i] > A[stack[-1]]:
        NGE[stack.pop()] = A[i]
 
    stack.append(i)

print(*NGE)