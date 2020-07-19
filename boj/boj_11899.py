# Silver 4

import sys

cnt = 0

s = list(sys.stdin.readline().rstrip())

top = s[::-1]

for i in range(len(s)-1, -1, -1):
    if top == "(" and s:
        cnt += 1
    elif top == ")":
        if top == s[::-1]:
            cnt += 1

    top = s.pop()

print(cnt)
