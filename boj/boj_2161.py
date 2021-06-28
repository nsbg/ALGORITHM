# Bronze 2

n = int(input())

cards = [i for i in range(1, n+1)]
abandoned = []

while len(cards) > 1:
    top = cards.pop(0)
    cards.append(cards.pop(0))
    abandoned.append(top)

for a in abandoned:
    print(a, end=' ')

print(cards[0])