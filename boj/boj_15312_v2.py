# Silver 5, 864ms

import sys

from string import ascii_uppercase

def calculate_compatibility(numbers):
    while len(numbers) > 2:
        # 일의 자리가 중요하기 때문에 10으로 나눈 나머지만 저장
        numbers = [((numbers[i] + numbers[i+1]) % 10) for i in range(len(numbers) - 1)]
    
    return "".join(map(str, numbers))

combined = []

strokes_number = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

strokes = {key: value for key, value in zip(list(ascii_uppercase), strokes_number)}

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

for a, b in zip(A, B):
    combined.append(strokes[a])
    combined.append(strokes[b])

compatibility = calculate_compatibility(combined)

print(compatibility)