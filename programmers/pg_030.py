def solution(a, b):
    answer = 0

    for aa, bb in zip(a, b):
        answer += aa * bb

    return answer