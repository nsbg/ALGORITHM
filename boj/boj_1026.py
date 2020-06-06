n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
bSort = b

a.sort()
bSort.sort(reverse=True)

for i in range(n):
    sum += a[i] * bSort[i]

print(sum)