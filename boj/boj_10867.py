import sys

n = int(sys.stdin.readline().rstrip())

# -1000 ~ +1000
numList = list(map(int, sys.stdin.readline().split()))

for i in sorted(list(set(numList))):
    print(i, end=' ')