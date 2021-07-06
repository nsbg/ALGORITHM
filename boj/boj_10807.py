# Bronze 2

n = int(input())
numList = list(map(int, input().split()))
v = int(input())

numDict = {}

for i in range(1, n+1):
    numDict[i] = 0

for nl in numList:
    if nl == v:
        numDict[nl] += 1

print(numDict[v])
