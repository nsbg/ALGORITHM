# Bronze 2

import sys

car = sys.stdin.readline().rstrip()

carNum = 1

cnt_c = 26
cnt_d = 10

if car[0] == 'c':
    carNum *= cnt_c
else:
    carNum *= cnt_d

for i in range(1, len(car)):
    if car[i] == car[i-1]:
        if car[i] == "c":
            carNum *= cnt_c-1
        else:
            carNum *= cnt_d-1
    else:
        if car[i] == "c":
            carNum *= cnt_c
        else:
            carNum *= cnt_d

print(carNum)