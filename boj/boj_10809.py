# Bronze 2
# 속도 느림
import string

s = list(input().lower())

lower = list(string.ascii_lowercase)

indexList = []

for i in lower:
    if i in s:
        indexList.append(s.index(i))
    else:
        indexList.append("-1")

print(*indexList, sep=" ")
