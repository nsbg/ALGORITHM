# Bronze 2

import string

answer = 0
alphabet = ["0"]+list(string.ascii_uppercase)

n = int(input())

name = list(input())

for i in name:
    answer += alphabet.index(i)

print(answer)