# Bronze 3

import sys

res = int(sys.stdin.readline())

book = []

for _ in range(9):
    book.append(int(input()))

print(res-sum(book))