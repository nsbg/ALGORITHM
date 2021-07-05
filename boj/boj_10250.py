# Bronze 3

import sys

t = int(input())

''' 
h: 호텔 층 수
w: 각 층의 방 수
n: 손님 순서
'''

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    unit = ""

    if n//h < 10:
        unit = "0"+str(n//h+1)
    else:
        unit = str(n//h+1)

    if n%h == 0:
        print(str(h)+str(n//h))
    else:
        print(str(n%h)+unit)
