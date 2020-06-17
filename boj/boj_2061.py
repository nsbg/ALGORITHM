import sys

k, l = map(int, input().split())

for i in range(2, l+1):
    if i == l:
        print("GOOD")
    elif k % i == 0:
        print("BAD", i)
        sys.exit()
#print(bad)

#if len(bad) > 0:
#    print("BAD", min(bad))
#elif len(bad) == 0:
#    print("GOOD")



