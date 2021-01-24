# Silver 5

n = int(input())

cnt = 0

for _ in range(n):
    word = input().lower()

    for i in range(len(word)):
        if i != len(word)-1:
            if word[i] != word[i+1]:
                if word[i] in word[i+2:]:
                    break
            else:
                pass
        else:
            cnt += 1

print(cnt)