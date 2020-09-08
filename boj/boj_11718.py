# Bronze 3
# sys.stdin : EOF 입력 받으면 종료

import sys

# splitlines() : 줄바꿈 제거해줌
word = sys.stdin.read().splitlines()

for i in word:
    print(i)

# sys 안 쓰고 input 쓰는 경우
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break