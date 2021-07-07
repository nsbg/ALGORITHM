# Bronze 2

t = int(input())

for _ in range(t):
    idx, words = input().split()
    print(words[:int(idx)-1]+words[int(idx):])