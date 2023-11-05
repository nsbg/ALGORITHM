# Bronze 2

import sys

from string import ascii_lowercase

L = int(input())

text = sys.stdin.readline().strip()

alphabet = [0]+list(ascii_lowercase)

result = 0

for i in range(len(text)):
    result += (alphabet.index(text[i])*(31**i))
    
print(result%1234567891)