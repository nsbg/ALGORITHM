# Bronze 1

import sys

n = int(sys.stdin.readline().rstrip())

snailPosX = 0
snailPosY = 0

go = 1

posChk = 0

direction = True

while True:
    # 위, 오른쪽 방향
    if direction:
        for _ in range(go):
            snailPosY += 1
            posChk += 1

            if posChk == n:
                print(snailPosX, snailPosY, sep=' ')

                # break 걸면 for 하나만 빠져나오고 exit()는 while 전체 빠져나옴
                exit()

        for _ in range(go):
            snailPosX += 1
            posChk += 1

            if posChk == n:
                print(snailPosX, snailPosY, sep=' ')
                exit()

    # 아래, 왼쪽 방향
    else:
        for _ in range(go):
            snailPosY -= 1
            posChk += 1

            if posChk == n:
                print(snailPosX, snailPosY, sep=' ')
                exit()

        for _ in range(go):
            snailPosX -= 1
            posChk += 1

            if posChk == n:
                print(snailPosX, snailPosY, sep=' ')
                exit()

    go += 1
    direction = not direction