# Silver 5

import sys

from string import ascii_lowercase, ascii_uppercase

'''
로직

리스트 정렬해서 같은지 비교
'''
uppercase_code = {key: value for key, value in zip(list(ascii_uppercase), range(1, 27))}
lowercase_code = {key: value for key, value in zip(list(ascii_lowercase), range(27, 53))}

uppercase_code.update(lowercase_code)

crypto_code = uppercase_code

crypto_code.update({' ': 0})
 
N = int(sys.stdin.readline().strip())

crypto = sorted(list(map(int, sys.stdin.readline().split())))

plain_text = sys.stdin.readline().strip()

encryption = sorted([crypto_code[key] for key in plain_text])

if crypto == encryption:
    print("y")
else:
    print("n")