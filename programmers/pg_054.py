# Level 2

def solution(numbers):
    strNumbers = list(map(str, numbers))
    
    strNumbers.sort(key = lambda x: x*4, reverse=True)
    
    return str(int(''.join(strNumbers)))