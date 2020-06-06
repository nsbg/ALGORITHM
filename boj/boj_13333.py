n = int(input())

p = list(map(int, input().split()))

p.sort(reverse=True)

qIndex = 0

for a in p:
    qIndex += int(a > qIndex)       # 이렇게 식 표현하면 True/False로 출력돼서 1, 0 더해줄 수 있음

print(qIndex)