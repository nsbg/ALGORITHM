# Bronze 1

n = int(input())

perimeter = [0] * (n+1)

perimeter[1] = 4
perimeter[2] = 6

for i in range(3, n+1):
    perimeter[i] = perimeter[i-1] + perimeter[i-2]

print(perimeter[n])