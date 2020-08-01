# Level 1

def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer

# 다른 풀이
# def sumDivisor(n):
#     return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
# 반만 검사하면 되기 때문에 성능 2배 향상