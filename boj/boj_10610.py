# Silver 5

number = input()
temp = 0

if '0' not in number:
    print(-1)
else:
    for n in number:
        temp += int(n)

    if temp%3 != 0:
        print(-1)
    else:
        numberList = sorted(number, reverse=True)
        print(''.join(numberList))