# Bronze 3

import sys

n, l, d = map(int, sys.stdin.readline().split())

music = []

# 노래 수만큼 반복
for i in range(n):

    # 한 곡 길이만큼 1로 바꿔줌
    for j in range(l):
        music.append(1)

    # 노래 안 나오는 동안 0으로 바꿔줌
    for k in range(5):
        music.append(0)

# 위 접근방식은 인터넷 참고

for i in range(len(music)):
    
