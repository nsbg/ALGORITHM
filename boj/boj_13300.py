# Bronze 2

N, K = map(int, input().split())

student_list = {key: [0, 0] for key in range(1, 7)}

room = 0

for _ in range(N):
    S, Y = map(int, input().split())
    
    if S == 0:
        student_list[Y][0] += 1
    else:
        student_list[Y][1] += 1

for key, value in student_list.items():
    if value[0] > K:
        if value[0]%K == 0:
            room += (value[0]//K)
        else:
            room += (value[0]//K)+1
    else:
        if value[0] > 0:
            room += 1
    
    if value[1] > K:
        if value[1]%K == 0:
            room += (value[1]//K)
        else:
            room += (value[1]//K)+1
    else:
        if value[1] > 0:
            room += 1
        
print(room)