# Bronze 1

import sys

n = int(input())

first = list(sys.stdin.readline().rstrip())

for _ in range(n-1):
    cmd = list(sys.stdin.readline().rstrip())

    for i in range(len(first)):
        if first[i] != cmd[i]:
            first[i] = "?"

print(''.join(first))