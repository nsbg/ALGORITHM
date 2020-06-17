from math import factorial

n, k = map(int, input().split())

print(factorial(n) // (factorial(k)*factorial(n-k)))

# / : 결과가 float로 나오는 나눗셈
# // : 결과가 int로 나오는 나눗셈

