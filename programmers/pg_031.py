def solution(arr, divisor):
    answer = []

    if divisor == 1:
        answer = sorted(arr)
    else:
        for a in arr:
            if a % divisor == 0:
                answer.append(a)

        if len(answer) == 0:
            answer.append(-1)

    return sorted(answer)