# Level 2

def solution(n):
    answer = ""
    oneTwoFour = ['4', '1', '2']

    if n <= 3:
        # 문자열의 (n%3)번째 요소
        answer = '412'[n % 3]
    else:
        while n > 0:
            answer = oneTwoFour[n % 3] + answer

            if n % 3 == 0:
                n = n // 3 - 1
            else:
                n //= 3

    return answer