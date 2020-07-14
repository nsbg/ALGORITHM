# Bronze 3

import sys

n, p = map(int, sys.stdin.readline().split())

pizza = []

for i in range(n):
    pizzaList = list(map(str, sys.stdin.readline().split()))
    pizza.append(int(pizzaList[0]))

myPizza = pizza[p-1]

pizza.remove(min(pizza))
pizza.remove(max(pizza))

avg = sum(pizza) / len(pizza)

if myPizza <= avg:
    print("YES")
else:
    print("NO")