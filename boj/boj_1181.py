# Silver 5

import sys

n = int(sys.stdin.readline().rstrip())

wordList = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    wordList.append((word, len(word)))

# lambda 인자가 여러 개 와야할 때는 괄호로 묶어주기
wordList = sorted(list(set(wordList)), key=lambda x: (x[1], x[0]))

for i in range(len(wordList)):
    print(wordList[i][0])