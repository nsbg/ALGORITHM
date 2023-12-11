# Bronze 3

import sys

T = int(sys.stdin.readline().strip())

check = T

# 300초, 60초, 10초
a, b, c = 0, 0, 0

if T%10 != 0:
    print(-1)
else:
    while check != 0:
        if check >= 300:
            quotient = check//300
            
            a += quotient

            check -= (quotient*300)
        elif check >= 60:
            quotient = check//60

            b += quotient

            check -= (quotient*60)
        else:
            quotient = check//10

            c += quotient

            check -= (quotient*10)

    print(a, b, c, sep=' ')