# Level 1

from string import ascii_lowercase

alphabet = list(ascii_lowercase)

def solution(s, skip, index):
    answer = ''
    
    new_alphabet = sorted(list(set(alphabet).difference(list(set(skip)))))

    for char in s:
        check = new_alphabet.index(char)+index

        if check > len(new_alphabet)-1:
            answer += new_alphabet[check%len(new_alphabet)]
        else:
            answer += new_alphabet[check]
              
    return answer