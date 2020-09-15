# Silver 3

n = int(input())


def fibo_7(num):
    res = 0

    fibo = [0] * (num+1)

    fibo[1] = 1
    fibo[2] = 1

    for i in range(3, len(fibo)):
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007

    res = fibo[num]

    return res


print(fibo_7(n))