# Bronze 5

import sys

N = int(sys.stdin.readline().strip())

default = 'long int'

additional_long_count = (N-4)//4

print('long '*additional_long_count+default)