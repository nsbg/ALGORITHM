from itertools import combinations

n, m = map(int, input().split())

maxSum = m

numList = list(map(int, input().split()))

c = list(combinations(numList, 3))

ans = []

for i in c:
    if sum(i) <= maxSum:
        ans.append(sum(i))
    elif sum(i) > maxSum:
        pass

ans.sort(reverse=True)

print(ans[0])
