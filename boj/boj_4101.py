import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))

    if sum(num) == 0:
        break

    if num[0] > num[1]:
        print("Yes")
    else:
        print("No")