# Bronze 4

ab = input()

if ab[1] == '0':
    print(10+int(ab[2:]))
elif ab[-1] == '0':
    print(int(ab[0])+10)
else:
    print(int(ab[0])+int(ab[1]))