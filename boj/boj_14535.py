import sys

#month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthList = []

while True:
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        d, m, y = map(int, sys.stdin.readline().split())
        monthList.append(m)

    for m in month:


    if n == 0:
        break