# Level 2
# 파이썬 내장 deque 안 쓰고 풀어봤음

def solution(priorities, location):
    # 문서 순서 저장
    d = [i for i in range(len(priorities))]

    # 출력 순서 저장
    result = []

    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            result.append(d.pop(0))
            priorities.pop(0)
        else:
            # 순서 밀리는 애들은 뒤로 보냄
            priorities.append(priorities.pop(0))
            d.append(d.pop(0))

    return result.index(location) + 1