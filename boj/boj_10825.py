# Silver 4

import sys

n = int(input())

student = []

for _ in range(n):
    student.append(sys.stdin.readline().split())

student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]),x[0]))

for s in student:
    print(s[0])