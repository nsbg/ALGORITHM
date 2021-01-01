# Level 2

def solution(n):
    answer = [0] * (n + 1)

    answer[0] = 0
    answer[1] = 1

    for i in range(2, n + 1):
        answer[i] = answer[i - 2] + answer[i - 1]

    return answer[n] % 1234567