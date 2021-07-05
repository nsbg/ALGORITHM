# Bronze 2

import sys

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
third = sys.stdin.readline().rstrip()

print((color.index(first)*10+color.index(second))*(10**color.index(third)))