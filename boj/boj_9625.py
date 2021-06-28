# Bronze 1

k = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, k):
    a[i] = a[i-2]+a[i-1]
    b[i] = b[i-2]+b[i-1]

print(a)
print(b)