# Level 1

def solution(n):
    answer = ""

    num = sorted(list(map(int, str(n))), reverse=True)

    for i in num:
        answer += str(i)

    return int(answer)