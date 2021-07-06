# Bronze 2
# ord() 쓰면 딕셔너리 안 쓰고 더 간단하게 만들기 ㄱㄴ

import sys, string

alphabetList = list(string.ascii_lowercase)
alphabetDict = {}

for a in alphabetList:
    alphabetDict[a] = 0

word = sys.stdin.readline().rstrip()

for w in word:
    if w in alphabetDict.keys():
        alphabetDict[w] += 1
    
for k in list(alphabetDict.values()):
    print(k, end=' ')