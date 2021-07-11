# Bronze 4

t = list(map(int, input().split()))

m = int(input())

if t[1]+m >= 60:
    while t[1]+m >= 60:
        t[1] = (t[1]+m)-60
        t[0] += 1
else:
    t[1] += m

if t[0] > 23:
    t[0] = 0
    
print(*t)