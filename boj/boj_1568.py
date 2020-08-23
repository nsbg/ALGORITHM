# Bronze 2

# 새의 수
n = int(input())

# 새가 부르는 숫자
k = 1

res = 0

while n > 0:
    if n >= k:
        n -= k
        k += 1
        res += 1
    else:
        k = 1

print(res)