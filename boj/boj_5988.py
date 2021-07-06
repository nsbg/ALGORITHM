# Bronze 2

n = int(input())

for _ in range(n):
    if input()[-1] in "02468":
        print("even")
    else:
        print("odd")