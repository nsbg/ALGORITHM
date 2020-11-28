# Bronze 1

import sys

for n in sys.stdin:
    n = int(n)

    if n % 6 == 0:
        print("Y")
    else:
        print("N")