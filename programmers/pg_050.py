def distance(num, hand):
    # 거리 구할 때 -> 일단 좌표로 생각해보기
    position = {1: [0, 0], 2: [1, 0], 3: [2, 0],
                4: [0, 1], 5: [1, 1], 6: [2, 1],
                7: [0, 2], 8: [1, 2], 9: [2, 2],
                '*': [0, 3], 0: [1, 3], '#': [2, 3]}

    newNum = position[num]
    currentHand = position[hand]

    return abs(newNum[0] - currentHand[0]) + abs(newNum[1] - currentHand[1])


def solution(numbers, hand):
    answer = ""

    currentLeft = "*"
    currentRight = "#"

    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            currentLeft = n
        elif n in [3, 6, 9]:
            answer += "R"
            currentRight = n
        elif n in [2, 5, 8, 0]:
            leftDistance = distance(n, currentLeft)
            rightDistance = distance(n, currentRight)

            if leftDistance == rightDistance:
                if hand == "left":
                    answer += "L"
                    currentLeft = n
                else:
                    answer += "R"
                    currentRight = n
            elif leftDistance < rightDistance:
                answer += "L"
                currentLeft = n
            else:
                answer += "R"
                currentRight = n

    return answer