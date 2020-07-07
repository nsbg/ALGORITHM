# Bronze 2

import sys

n = int(input())

for _ in range(n):
    carNumber = sys.stdin.readline().rstrip().split('-')

    three = 0

    for i, n in enumerate(carNumber[0][::-1]):
        # ord() -> 문자의 아스키코드 값 반환
        three += (ord(n)-65)*(26**i)

    if abs(three-int(carNumber[1])) <= 100:
        print("nice")
    else:
        print("not nice")