import sys

n = int(sys.stdin.readline().rstrip())

see = []

cnt = 1

for _ in range(n):
    h = int(sys.stdin.readline().rstrip())

    see.append(h)

maxStick = see[len(see)-1]

for i in range(len(see)-1, 0, -1):
    if see[i-1] > maxStick:
        cnt += 1
        maxStick = see[i-1]

print(cnt)