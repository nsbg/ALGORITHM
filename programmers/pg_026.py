def solution(n):
    fibo = [1, 2] + [0] * (n - 2)

    for i in range(2, len(fibo)):
        fibo[i] = (fibo[i - 2] + fibo[i - 1]) % 1000000007

    return fibo[i]