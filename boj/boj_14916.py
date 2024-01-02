# Silver 5

import sys

N = int(sys.stdin.readline().strip())

answer = 0

# 5보다 작은 경우
if N<5:
    if N%2 == 0:
        answer += N//2
    else:
        print("-1")
        exit()


if N%5 == 0:                # 5의 배수인 경우
    answer += N//5
elif N>5 and (N%5)%2 == 0:  # 5보다 크고 5로 나눈 나머지가 짝수인 경우 ex) 12
    answer += N//5

    N -= (N//5)*5

    answer += N//2
elif N>5 and (N%5)%2 != 0:  # 5보다 크고 5로 나눈 나머지가 홀수인 경우 ex) 13
    temp = N//5

    answer += temp-1

    N -= (temp-1)*5

    answer += N//2

print(answer)