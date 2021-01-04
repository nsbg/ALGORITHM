def solution(arr):
    answer = arr
    answer.remove(min(arr))

    if len(answer) < 1:
        answer.append(-1)

    return answer