# Silver 2

import sys

K = int(input())

def checkWhiteSpace(str):
    newStr = ''

    for i in range(len(str)-1):
        if str[i] in ['(', ')', ',', '.', ':']:
            if i > 0 and str[i-1] == ' ':
                newStr += '-'
            if str[i+1] == ' ':
                newStr += '-'
        else:
            newStr += str[i]

    newStr = newStr.replace('-', '')

    return newStr

for i in range(K):
    s1 = sys.stdin.readline().strip().lower()
    s2 = sys.stdin.readline().strip().lower()
    
    s1 = s1.replace('{', '(').replace('[', '(').replace(']', ')').replace('}', ')').replace(';', ',')
    s2 = s2.replace('{', '(').replace('[', '(').replace(']', ')').replace('}', ')').replace(';', ',')

    s1 = checkWhiteSpace(s1)
    s2 = checkWhiteSpace(s2)

    s1 = ' '.join(s1.split())
    s2 = ' '.join(s2.split())
    
    if s1 == s2:
        if i != K-1:
            print("Data Set "+str(i+1)+": equal\n")
        else:
            print("Data Set "+str(i+1)+": equal", end='')
    else:
        if i != K-1:
            print("Data Set "+str(i+1)+": not equal\n")
        else:
            print("Data Set "+str(i+1)+": not equal", end='')