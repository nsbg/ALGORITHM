# Silver 5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n*factorial(n-1) 

N = int(input())

cnt = 0

for i in str(factorial(N))[::-1]:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)