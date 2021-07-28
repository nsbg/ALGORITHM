# Bronze 2

import sys

while True:
    crypto = sys.stdin.readline().rstrip()

    if crypto == 'END':
        break

    print(crypto[::-1])