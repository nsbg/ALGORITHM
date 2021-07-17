# Silver 5

n = list(map(int, input()))
cnt = 0

y = [3, 6, 9]

while True:
    if len(n) == 1:
        print(cnt)

        if int(n[0]) in y:
            print("YES")
            break
        else:
            print("NO")
            break
    
    n = list(map(int, list(str(sum(n)))))

    cnt += 1

