# Silver 4

book = {}

n = int(input())

for _ in range(n):
    name = input()

    if name not in book.keys():
        book[name] = 1
    else:
        book[name] += 1
    
best = []

for k, v in book.items():
    if v == max(book.values()):
        best.append(k)

print(sorted(best)[0])