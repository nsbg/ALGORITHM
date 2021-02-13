def solution(n, arr1, arr2):
    answer = []

    tmp = 0

    for a1, a2 in zip(arr1, arr2):
        res = ""
        tmp = a1 | a2
        tmp = str(bin(tmp))[2:].zfill(n)

        for t in tmp:
            if t == "0":
                res += " "
            else:
                res += "#"

        answer.append(res)

    return answer