# Bronze 5

import sys

time = 0

for _ in range(4):
    time += int(sys.stdin.readline().rstrip())

print(time // 60)
print(time % 60)