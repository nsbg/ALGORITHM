# Level 1

def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    return list(sorted(set(answer)))