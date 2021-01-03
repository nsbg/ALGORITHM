def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    oneScore = 0
    twoScore = 0
    threeScore = 0

    for i in range(0, len(answers)):
        if answers[i] == one[i % 5]:
            oneScore += 1
        if answers[i] == two[i % 8]:
            twoScore += 1
        if answers[i] == three[i % 10]:
            threeScore += 1

    answer = [oneScore, twoScore, threeScore]
    result = []

    for i, v in enumerate(answer):
        if v == max(answer):
            result.append(i + 1)

    return result