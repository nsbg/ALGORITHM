import sys

n, r = map(int, sys.stdin.readline().split())

if n == 0 and r == 0:
    print("Not a moose")
else:
    if n == r:
        print("Even", n+r, sep=' ')
    elif n >= r:
        print("Odd", n*2, sep=' ')
    elif n <= r:
        print("Odd", r*2, sep=' ')