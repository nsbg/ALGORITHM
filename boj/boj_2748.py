# Silver 5

n = int(input())


def fibo_2(num):

    fibo = [0] * (num+3)

    fibo[1] = 1
    fibo[2] = 1

    for i in range(3, len(fibo)):
        fibo[i] = fibo[i-1] + fibo[i-2]

    return fibo[num]


print(fibo_2(n))