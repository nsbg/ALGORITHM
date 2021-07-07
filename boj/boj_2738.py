# Bronze 1

n, m = map(int, input().split())

a, b = [], []

for _ in range(n):
    a.append(list(map(int, input().split())))
    
for _ in range(m):
    b.append(list(map(int, input().split())))

# for i in [a, b]:
#   for j in range(n):
#       i.append(list(map(int, input().split())))
# => 위와 동일한 코드

for j in range(n):
    for k in range(m):
        a[j][k] += b[j][k]
    
    print(*a[j])
