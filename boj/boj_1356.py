# Bronze 1

import sys

n = sys.stdin.readline().rstrip()

chk = 0

for i in range(len(n)-1):
    front = 1
    rear = 1

    # 앞 부분 곱 체크
    for f in range(i+1):
        front *= int(n[f])

    # 뒷 부분 곱 체크
    for r in range(i+1, len(n)):
        rear *= int(n[r])

    if front == rear:
        chk = 1
        break

if chk == 1:
    print("YES")
else:
    print("NO")