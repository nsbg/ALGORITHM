# Level 1

def solution(s):
    answer = ''
    
    num_str = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
               'seven', 'eight', 'nine']
    
    num_dict = {key: value for value, key in enumerate(num_str)}
    
    temp = ''
    
    for alphabet in s:
        if alphabet.isdigit() == False:
            temp += alphabet
        else:
            answer += alphabet
            
        if temp in num_dict.keys():
            answer += str(num_dict[temp])
            temp = ''

    return int(answer)