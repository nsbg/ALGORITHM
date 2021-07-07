# Bronze 3

t = int(input())

for _ in range(t):
    answer = 0
    
    num = list(map(int, input().split()))

    even = max(num)

    for n in num:
        if n%2 == 0:
            answer += n

            if n < even:
                even = n
    
    print(answer, even)