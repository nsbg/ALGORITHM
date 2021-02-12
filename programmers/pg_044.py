def solution(N, stages):
    stageList = {}
    challenger = len(stages)

    for s in range(1, N + 1):
        if challenger == 0:
            stageList[s] = 0
            continue

        trying = stages.count(s)

        # 딕셔너리 값 지정 굳이 update() 쓸 필요 X
        stageList[s] = trying / challenger
        challenger -= trying

    answer = sorted(stageList, reverse=True, key=lambda x: stageList[x])

    return answer