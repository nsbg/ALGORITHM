# Silver 3

p = [0]*101

p[1] = 1
p[2] = 1
p[3] = 1

t = int(input())

for i in range(t):
    n = int(input())

    for j in range(4, n+1):
        p[j] = p[j-3]+p[j-2]

    print(p[n])