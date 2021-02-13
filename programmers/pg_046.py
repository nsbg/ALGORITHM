def solution(s, n):
    result = ""

    for ss in s:
        if ss.isupper():
            result += chr(ord(ss) + n) if ord(ss) + n <= 90 else chr(ord(ss) + n - 26)
        elif ss.islower():
            result += chr(ord(ss) + n) if ord(ss) + n <= 122 else chr(ord(ss) + n - 26)
        else:
            result += " "

    return result