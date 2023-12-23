# Silver 5

import sys

# TODO: A진법을 B진법으로 바꾸는 것
A, B = map(int, sys.stdin.readline().split())

# A진법으로 나타낸 숫자의 자리수 개수
m = int(sys.stdin.readline().strip())

# A진법을 이루고 있는 숫자 m개 높은 자릿수부터 주어짐
number = list(map(int, sys.stdin.readline().split()))

# number를 10진법으로 바꾸고 그 수를 B진법으로 분해
number.reverse()

base_10 = 0

for i in range(len(number)):
    base_10 += (number[i]*(A**i))

base_B = []

while base_10:
    base_B.append(base_10%B)

    base_10 = base_10//B
    
print(*base_B[::-1], sep=' ')