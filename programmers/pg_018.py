# Level 1

def solution(array, commands):
    answer = []

    for c in commands:
        temp = sorted(array[c[0] - 1:c[1]])
        answer.append(temp[c[2] - 1])

    return answer