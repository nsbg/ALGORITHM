# Bronze 1
# 0이면 번, 1이면 데기 부른 사람을 알아내는 것

import sys

# 번
zero = [0]
zeroCnt = 0

# 데기
one = [1]
oneCnt = 0

# 회차 체크
chk = 1

a = int(input())
t = int(input())
what = int(input())

play = [0, 1, 0, 1]

if t == 0:
    print("0")
else:
    index = 0

    while True:
        chk += 1

        res = play+(zero*chk)+(one*chk)

        for r in res:
            index += 1

            if what == 0 and r == 0:
                    zeroCnt += 1

                    if zeroCnt == t:
                        print((index-1) % a)
                        exit()

            elif what == 1 and r == 1:
                    oneCnt += 1

                    if oneCnt == t:
                        print((index-1) % a)
                        exit()