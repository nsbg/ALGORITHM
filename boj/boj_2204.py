firstWordList = []

while True:
    # while문 안인지 밖인지 위치 중요할 때가 있음
    wordList = []

    n = int(input())

    if n == 0:
        break

    for _ in range(n):
        wordList.append(input())

    # 소문자 우선 정렬
    wordList.sort(key=lambda x: x.lower())

    firstWordList.append(wordList[0])

print(*firstWordList, sep='\n')