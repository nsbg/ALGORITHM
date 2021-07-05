# Bronze 3

addition = []

for i in range(7):
    n = int(input())

    if n%10 not in [0, 2, 4, 6, 8]:
        addition.append(n)

addition = sorted(addition)

print(sum(addition))
print(addition[0])