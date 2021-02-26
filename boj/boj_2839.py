# Bronze 1

import sys

n = int(sys.stdin.readline().rstrip())
count = 0

while True:
    if n < 0:
        count = -1
        break

    if n % 5 == 0:
        count += n//5
        break
    else:
        count += 1
        n -= 3

print(count)