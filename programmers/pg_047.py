# re 모듈 안 쓰려고 하다보니까 코드가 길어졌지만 re 모듈도 한번은 공부해놓기
def solution(new_id):
    answer = ''
    accepted = [i for i in range(0, 10)] + ['-', '_', '.'] + [chr(j) for j in range(97, 123)]

    accepted = list(map(str, accepted))
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] in accepted:
            answer += new_id[i]

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer[1:] if answer[0] == "." and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == "." else answer

    if len(answer) == 0:
        answer += "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer