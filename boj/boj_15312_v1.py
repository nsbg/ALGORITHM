# Silver 5, 4192ms

import sys

from string import ascii_uppercase

'''
로직

1. 이름을 번갈아가면서 쓰고 각 획수 리스트로 변환 -> [1, 3, 2, 3, 2, 2] 처럼
2. 두 개씩 더하면서 빠른 인덱스를 갱신 -> 0번 인덱스, 1번 인덱스 합을 0번 인덱스에 저장하는 방식 -> [4, 5, 5, 5, 4]
3. 리스트에 숫자 두 개가 남을 때까지 2번 반복
'''
stroke_number = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

alphabet = {key: value for key, value in zip(list(ascii_uppercase), stroke_number)}

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

name_rearrange = ""

for a, b in zip(A, B):
    name_rearrange += (a+b)

name_stroke = [alphabet[value] for value in name_rearrange]

i = 1

while True:
    if len(name_stroke) == 2:
        break
    
    try:
        name_stroke[i-1] = name_stroke[i-1]+name_stroke[i]
        i += 1
    except IndexError:
        name_stroke = name_stroke[:len(name_stroke)-1]
        
        for j in range(len(name_stroke)):
            if name_stroke[j] >= 10:
                name_stroke[j] = int(str(name_stroke[j])[-1])
        i = 1

print(*name_stroke, sep='')