# Bronze 1

import sys

idx = 0

answer = 0

while True:
    # V일짜리 휴가를 받았을 때, 연속하는 P일 중 L일 동안만 사용 가능
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    idx += 1
    
    if V%P >= L:
        temp = L
    else:
        temp = V%P

    answer = (V//P*L+temp)

    print(f"Case {idx}: {answer}")