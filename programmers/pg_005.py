# Level 1

def solution(s):
    answer = ''

    if len(s) % 2 != 0:
        i = len(s) // 2
        answer += s[i]
    else:
        i = len(s) // 2 - 1
        answer += s[i:i+2]

    return answer