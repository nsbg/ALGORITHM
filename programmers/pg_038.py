def solution(x, n):
    answer = []

    for i in range(n, 0, -1):
        answer.append(x * i)

    if x < 0:
        return sorted(answer, reverse=True)
    else:
        return sorted(answer)