# 문제 이해도 어려웠다.. 다른 언어로 풀 땐 처음부터 다시 생각해보기
def solution(citations):
    # [0, 1, 3, 5, 6]
    citations.sort()

    hIndex = 0

    for i in range(len(citations)):
        # citations[i] : 논문 인용 횟수
        # len(citations)-i : citations[i]번 이상 인용된 논문 수
        if citations[i] >= len(citations) - i:
            return len(citations) - i

    return hIndex