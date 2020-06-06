k, l = map(int, input().split())

bad = []

for i in range(2, l):
    if k % i == 0:
        bad.append(i)

if len(bad) > 0:
    print("BAD", min(bad))
elif len(bad) == 0:
    print("GOOD")



