alphabetList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = input()

res = 0

for i in range(len(s)):                         # s 길이만큼 반복
    for j in alphabetList:                      # alphabetList에서 하나씩 꺼냄
        if s[i] in j:                           # s 안에 있는 글자 하나하나가 j에 있을 경우
             res += alphabetList.index(j) + 3   # 1이 2초가 걸리는데 인덱스는 0부터니까 3을 더해줌

print(res)
