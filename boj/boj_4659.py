import sys

vowel = ['a', 'e', 'i', 'o', 'u']

while True:

    check_Vowel = 0
    check_Consecutive = 0

    pw = sys.stdin.readline().rstrip()

    if pw == "end":
        break

    # 모음 존재 여부 확인
    for c in pw:
        if c in vowel:
            check_Vowel = 1

    # 연속 3 모음, 3 자음 확인
    for i in range(len(pw)-2):
        if pw[i] in vowel and pw[i+1] in vowel and pw[i+2] in vowel:
            check_Consecutive = 1
        elif pw[i] not in vowel and pw[i+1] not in vowel and pw[i+2] not in vowel:
            check_Consecutive = 1

    # 같은 알파벳 연속인지 확인
    for i in range(len(pw) - 1):
        if pw[i] not in 'eo':
            if pw[i] == pw[i + 1]:
                check_Consecutive = 1

    # 모음이 없거나 연속하는 알파벳이 있는 경우
    if check_Vowel == 0 or check_Consecutive == 1:
        print("<"+pw+">", "is not acceptable.")
    # 아닌 경우
    else:
        print("<"+pw+">", "is acceptable.")