n = int(input())

mirror = [input() for _ in range(n)]

k = int(input())

if k == 1:
    for m in mirror:
        print(m)
elif k == 2:
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(mirror[i][j], end='')
        print()
elif k == 3:
    # mirror 입력 받을 때 문자열로 입력 받았기 때문에
    print(*mirror[::-1], sep='\n')