# Silver 4

n = int(input())
num = list(map(int, input().split()))

answer = 0

for number in num:
    cnt = 0
    
    for i in range(2, number+1):
        if number%i == 0:
            cnt += 1
    
    if cnt == 1:
        answer += 1

print(answer) 