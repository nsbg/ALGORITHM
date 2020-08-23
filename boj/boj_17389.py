# Bronze 2

import sys

n = int(input())

s = sys.stdin.readline().rstrip()

res = 0
bonus = 0

for i in range(len(s)):
    if s[i] == 'O':
        res += (i+1)+bonus
        bonus += 1
    else:
        bonus = 0

print(res)