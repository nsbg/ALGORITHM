# Silver 5

n = int(input())

num = [i for i in range(1, n+1)]

end = 0
cnt = 0
total = 0

for start in range(len(num)):
    while total < n and end < len(num):
        total += num[end]
        end += 1
    
    if total == n:
        cnt += 1
    
    print("-= num[start] 전:", str(total))
    total -= num[start]
    print("-= num[start] 후", str(total))

print(cnt)