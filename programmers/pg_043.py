def solution(n, m):
    answer = []

    mul = n * m

    # 유클리드 호제법
    while n > 0:
        tmp = n
        n = m % n
        m = tmp

    answer += [tmp, mul / tmp]

    return answer