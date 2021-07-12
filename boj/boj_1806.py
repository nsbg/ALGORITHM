# Gold 4

n, s = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 0, 0

total = 0

answer = 100001

while True:
    if total >= s:
        total -= arr[start]
        answer = min(answer, end-start)
        start += 1
    else:
        if end == n:
            break
        else:
            total += arr[end]
            end += 1

if answer == 100001:
    print(0)
else:
    print(answer)