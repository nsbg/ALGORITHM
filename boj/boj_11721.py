# Bronze 2

import sys

words = sys.stdin.readline().rstrip()

for i in range(0, len(words), 10):
    print(words[i:i+10])