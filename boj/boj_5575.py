# Bronze 4

work = []
answer = []

for _ in range(3):
    work.append(list(map(int, input().split())))

for w in work:
    sec = w[5]-w[2]
    min = w[4]-w[1]
    hour = w[3]-w[0]

    if sec < 0 and min <= 0:
        sec += 60
        min += 59
        hour -= 1
    elif sec < 0 and min > 0:
        sec += 60
        min -= 1
    elif sec >=0 and min < 0:
        min += 60
        hour -= 1
    
    answer.append([hour, min, sec])

for a in answer:
    print(*a)
