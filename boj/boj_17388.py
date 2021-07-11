# Bronze 4

univ = list(map(int, input().split()))

if sum(univ) >= 100:
    print("OK")
else:
    if univ.index(min(univ)) == 0:
        print("Soongsil")
    elif univ.index(min(univ)) == 1:
        print("Korea")
    else:
        print("Hanyang")