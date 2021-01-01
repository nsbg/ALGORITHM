# Level 2
# Level 2 치고는 많이 쉬운 듯 ,,?

def solution(s):
    answer = ''

    listS = list(map(str, s.split(' ')))

    for i in range(0, len(listS)):
        listS[i] = listS[i].capitalize()

    return ' '.join(listS)