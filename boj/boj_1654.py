# Silver 3

k, n = map(int, input().split())

line = sorted([int(input()) for _ in range(k)])

left = 1
right = max(line)

while left <= right:
    mid = (left+right)//2

    ans = 0
    ans += sum([l//mid for l in line])

    if ans >= n:
        left = mid+1
    else:
        right = mid-1

print(right)