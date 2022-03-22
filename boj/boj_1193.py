# Bronze 1

import sys

line_idx = 1 # 홀수번째 사선, 짝수번째 사선 판별
end_num = 0  # 각 사선이 끝나는 번호(1, 3, 6, 10 , ...)

X = int(input())

while X > line_idx:
    X -= line_idx
    line_idx += 1

if line_idx % 2 == 0:
    n = X
    d = line_idx-X+1
else:
    n = line_idx-X+1
    d = X

print(n, d, sep='/')
