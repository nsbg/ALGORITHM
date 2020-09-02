# 연습문제

def solution(d, budget):
    answer = 0
    res = 0

    d.sort()

    for i in d:
        if res + i <= budget:
            res += i
            answer += 1
        else:
            break

    return answer