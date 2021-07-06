# Silver 4

import sys

s = sys.stdin.readline().rstrip()

suffix = []

for i in range(0, len(s)):
    suffix.append(s[i:])

print(sorted(suffix))