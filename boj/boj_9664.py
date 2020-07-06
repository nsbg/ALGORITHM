# Bronze 3

import sys

n = int(sys.stdin.readline().rstrip())
o = int(sys.stdin.readline().rstrip())

# 막내딸이 몇 개를 가져갔는지 모르는 상태
p = o // (n-1)

# 막내딸이 본인 제외 다른 딸들과 동일하게 가져간 경우
if o-(p*(n-1)) == 0:
    print(o+p-1, o+p, sep=' ')
# 동일하지 않을 때
else:
    print(o+p, o+p, sep=' ')