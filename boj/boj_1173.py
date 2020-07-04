# Bronze 2

import sys

# N = 운동 횟수라고 생각하면 됨
N, m, M, T, R = map(int, sys.stdin.readline().split(' '))

ans = 0
exerciseCnt = 0
pulse = m

if M-m < T:
    print("-1")
    exit()

while True:
    if exerciseCnt == N:
        break
    # exerciseCnt != N
    else:
        if pulse + T <= M:
            pulse += T
            exerciseCnt += 1
        else:
            pulse -= R
            if pulse < m:
                pulse = m

    ans += 1

print(ans)