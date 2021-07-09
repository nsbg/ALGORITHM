# Silver 4

n = int(input())
m = int(input())

cnt = 0

start, end = 0, n-1

armor = sorted(list(map(int, input().split())))

while start < end and end < n:
    total = armor[start]+armor[end]

    if total < m:
        start += 1
    elif total > m:
        end -= 1
    else:
        cnt += 1
        start += 1

print(cnt)