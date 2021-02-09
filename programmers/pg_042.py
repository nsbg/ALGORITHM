def solution(n):
    # 시간이 오래 걸림
    answer = n

    num = [0, 0, 2] + [i for i in range(3, n + 1)]

    for nn in range(2, n + 1):
        for i in range(nn ** 2, len(num), nn):
            num[i] = 0

    answer -= num.count(0)

    return answer+1