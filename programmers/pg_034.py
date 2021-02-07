def solution(participant, completion):
    ''' 효율성 테스트 통과 X(시간 초과)
    for c in completion:
        if c in participant:
            participant.remove(c)

    return participant[0]'''

    '''
    remove : 시간 복잡도 O(n)
    -> for문 안으로 들어가면 O(n^2)
    '''

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    # 동명이인이 없는 경우 -> 짝 지어지지 않을 때
    return participant[-1]