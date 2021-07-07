# Bronze 2

n = list(map(int, input()))

if sum(n[:len(n)//2]) == sum(n[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")