# Bronze 1

import sys

s = sys.stdin.readline().rstrip()

resList = []

# 첫번째 단어
for i in range(0, len(s)-2):
    # 두번째 단어
    for j in range(i+1, len(s)-1):
        one = s[i::-1]
        two = s[j:i:-1]
        three = s[len(s)-1:j:-1]

        res = one+two+three

        resList.append(res)

print(sorted(resList)[0])