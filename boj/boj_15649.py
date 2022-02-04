# Silver 3

import sys

N, M = map(int, sys.stdin.readline().split())

# DFS → 스택 역할
arr = []

def DFS():
    # M개 모두 선택했을 때 출력(종료)
    if len(arr) == M:
        print(*arr, sep=' ')
        return
    
    for i in range(1, N+1):
        # arr 안에 없는 숫자일 경우에만 append(중복 없다는 조건 충족하기 위해)
        if i not in arr:
            arr.append(i)
            DFS()
            arr.pop()

DFS()