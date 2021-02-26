# Silver 3

t = int(input())

for i in range(t):
    n = int(input())

    oneTwoThree = [1, 2, 4] + [0] * (n-1)

    for j in range(3, n+1):
        oneTwoThree[j] = oneTwoThree[j-1] + oneTwoThree[j-2] + oneTwoThree[j-3]

    print(oneTwoThree[n-1])