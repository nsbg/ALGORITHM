# Level 1

# isdigit() : 문자열이 숫자인지 아닌지 T/F로 리턴
# 파이썬 삼항연산자 : condition and T or F

def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)