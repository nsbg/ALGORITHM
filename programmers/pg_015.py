# Level 1

def solution(s):
    makeList = s.split(' ')

    result = []

    for ml in makeList:
        whitespace = ''

        for i in range(len(ml)):
            if i % 2 == 0:
                whitespace += ml[i].upper()
            else:
                whitespace += ml[i].lower()

        result.append(whitespace)

    return ' '.join(result)