# 파이썬 말고 다른 언어로 풀 때는 알고리즘 구상 100% 혼자 하기
# TC 3, 7, 12 통과 X -> TC 7, 11 통과 X -> TC 11 통과 X
def solution(n, lost, reserve):
    answer = 0

    for l in range(1, n + 1):
        if l in reserve and l in lost:
            lost.remove(l)
            reserve.remove(l)

    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
                lost.remove(i)
            elif i + 1 in reserve:
                reserve.remove(i + 1)
                lost.remove(i)

    answer = n - len(lost)

    return answer