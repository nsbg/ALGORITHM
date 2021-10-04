# Silver 5

import sys
from string import ascii_lowercase

n = int(sys.stdin.readline().rstrip())

words = list(sys.stdin.readline().split())

alphabet = list(ascii_lowercase)
result = []

for w in words:
    if len(w) % 2 != 0:
        check = len(w)-1
    else:
        check = len(w)
    
    encrypto = ''

    for i in range(0, check, 2):
        calc = (alphabet.index(w[i])+alphabet.index(w[i+1])-n)%26
        encrypto += alphabet[calc]

    result.append(encrypto)

for r in result:
    print(r, end=' ')