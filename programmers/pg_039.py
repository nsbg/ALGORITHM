def solution(x):
    answer = True
    x = str(x)

    total = sum(list(map(int, x)))

    if int(x) % total == 0:
        answer
    else:
        answer = False

    return answer