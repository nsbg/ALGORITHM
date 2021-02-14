def solution(dartResult):
    answer = []
    score = ''

    for d in dartResult:
        if d.isnumeric():
            score += d

        elif d == "S":
            answer.append(int(score))
            score = ''
        elif d == "D":
            answer.append(int(score) ** 2)
            score = ''
        elif d == "T":
            answer.append(int(score) ** 3)
            score = ''

        elif d == "*":
            if len(answer) > 1:
                answer[-2] *= 2

            # 앞에서 접근할 경우 길이가 1일 때 index out of range
            answer[-1] *= 2

        elif d == "#":
            answer[-1] *= -1

    return sum(answer)