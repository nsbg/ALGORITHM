# Level 1

def solution(survey, choices):
    answer = ''
    
    type = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    
    score = {key: 0 for key in type}
    
    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += (4-c)
        else:
            score[s[1]] += (c-4)
    
    score_list = list(score.items())
    
    for i in range(0, len(score_list), 2):
        prev = score_list[i]
        post = score_list[i+1]

        if prev[1] >= post[1]:
            answer += prev[0]
        else:
            answer += post[0]
            
    return answer