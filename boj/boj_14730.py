# Bronze 1

n = int(input())

answer = 0

for _ in range(n):
    c, k = map(int, input().split())

    answer += c*k

print(answer)