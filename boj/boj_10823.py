# Bronze 1

answer = ''

while True:
    try:
        temp = input()
        answer += temp
    except:
        break

print(sum(list(map(int, answer.split(',')))))