def solution(arr1, arr2):
    answer = []
    temp = []

    for a, b in zip(arr1, arr2):
        for aa, bb in zip(a, b):
            temp.append(aa + bb)

        answer.append(temp)
        temp = []

    return answer