# Bronze 2

num = []

for _ in range(5):
    num.append(int(input()))

num = sorted(num)

print(sum(num)//5)
print(num[2])