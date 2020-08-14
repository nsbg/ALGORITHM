# Bronze 3

import sys

test_case = int(input())

for i in range(test_case):
    white_space = sys.stdin.readline().rstrip()

    res = 0

    t = int(sys.stdin.readline().rstrip())

    for j in range(t):
        cnt = int(sys.stdin.readline().rstrip())

        res += cnt

    if res % t == 0:
        print("YES")
    else:
        print("NO")