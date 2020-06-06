import sys

win = []

for _ in range(5):
    contestant = list(map(int, sys.stdin.readline().split()))
    win.append(sum(contestant))

print(win.index(max(win))+1, max(win), sep=' ')