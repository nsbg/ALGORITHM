# Silver 5

import sys

'''
로직

1. s, t 길이 확인
2. 두 문자열의 길이를 일치시켜서 같은지 확인
'''

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

s_len, t_len = len(s), len(t)

if s*t_len == t*s_len:
    print(1)
else:
    print(0)