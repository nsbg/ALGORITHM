# Gold 3

def primeNum(N):
    num = [1]*(N+1)

    d = int(n**0.5)

    for i in range(2, d+1):
        if num[i] == 1:
            for j in range(i+i, N+1, i):
                num[j] = 0

    return [p for p in range(2, n+1) if num[p] == 1]


n = int(input())

answer = 0
end, total = 0, 0

numList = primeNum(n)

for start in range(len(numList)):
    while total < n and end < len(numList):
        total += numList[end]
        end += 1

    if total == n:
    	answer += 1
    
    total -= numList[start]

print(answer)