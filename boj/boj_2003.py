# Silver 3

cnt = 0

n, m = map(int, input().split())

a = list(map(int, input().split()))

total = 0

start, end = 0, 0

while start <= end and end <= len(a):
    total = sum(a[start:end])

    if total > m:
        start += 1
    elif total < m:
        end += 1
    else:
        cnt += 1
        end += 1

print(cnt)