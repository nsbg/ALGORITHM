# Level 1

def solution(food):
    half_answer = ''
    
    for idx, value in enumerate(food[1:]):
        if value%2 != 0:
            half_answer += str(idx+1)*((value-1)//2)
        else:
            half_answer += str(idx+1)*(value//2)

    half_answer += '0'

    answer = half_answer+half_answer[-2::-1]
        
    return answer