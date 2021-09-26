# Bronze 2

import sys

score = list(map(int, sys.stdin.readline().split()))

hongik = int(input())

if hongik in score[:5]:
    print("A+")
elif hongik in score[:15]:
    print("A0")
elif hongik in score[:30]:
    print("B+")
elif hongik in score[:35]:
    print("B0")
elif hongik in score[:45]:
    print("C+")
elif hongik in score[:48]:
    print("C0")
else:
    print("F")