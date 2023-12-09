# Bronze 1

import sys

total_string = []

result = ''

for _ in range(5):
    total_string.append(list(sys.stdin.readline().strip()))

max_length = max(map(len, total_string))

for i in range(max_length):
    for j in range(5):
        try:
            result += total_string[j][i]
        except:
            continue

print(result)