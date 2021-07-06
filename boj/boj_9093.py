# Bronze 1

import sys

n = int(input())

for i in range(n):
    sentence = sys.stdin.readline().split()
    answer = []

    for s in sentence:
        reversedSentence = s[::-1]
        answer.append(reversedSentence)

print(' '.join(answer))