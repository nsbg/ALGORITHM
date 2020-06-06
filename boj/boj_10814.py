# 메모리 54016KB
# 시간 4376ms
# 코드 길이 237B
# 답은 맞았지만 메모리/시간 낭비 심한 코드

import sys

member = []

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    memberList = list(map(str, input().split()))
    member.append(memberList)

member.sort(key=lambda x: int(x[0]))

for k, v in member:
    print(k, v)
