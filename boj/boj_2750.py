# Bronze 1

n = int(input())
numberList = []

for _ in range(n):
    num = int(input())
    numberList.append(num)

for j in sorted(numberList):
    print(j)