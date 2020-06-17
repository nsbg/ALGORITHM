import sys

# 팁 : 원래 주려고 생각한 돈 - (받은 등수 - 1)
n = int(sys.stdin.readline().rstrip())

result = 0

tip = 0

waitLine = [0] + list(map(int, input()))

# 원래 주려고 생각한 돈 < 받은 등수 - 1

for i in range(1, n+1):
    if waitLine[i] < waitLine.index(waitLine[i]) - 1:
        tip = 0
    else:
        tip = waitLine[i] - waitLine.index(i)

    result += tip

print(result)

