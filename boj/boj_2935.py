# Bronze 3

import sys

a = int(sys.stdin.readline().rstrip())

operator = sys.stdin.readline().rstrip()

b = int(sys.stdin.readline().rstrip())

if operator == "*":
    print(a*b)
else:
    print(a+b)
