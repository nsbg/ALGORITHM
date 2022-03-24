# Silver 4
# Circular queue

import sys

N, K = map(int, sys.stdin.readline().split())

front = 0 # 삽입할 데이터가 없기 때문에 rear 역할 없어도 됨

josephus = [i for i in range(1, N+1)]

arr = []

while len(josephus) != 0:
    front += K-1
    arr.append(str(josephus.pop(front)))

print("<", ", ".join(a for a in arr)+">", sep="")