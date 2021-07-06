# Bronze 2

from abc import abstractproperty


n = int(input())

student = {}

for _ in range(n):
    name, score = map(str, input().split())
    student[name] = int(score)

maxCnt = 0
maxScore = max(student.values())

for s in student.values():
    if s == maxScore:
        maxCnt += 1

for k, v in student.items():
    if maxCnt == 1:
        if v == maxScore:
            print(k)
    else:
        student = sorted(student)
        print(student[0])
        break