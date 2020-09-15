# Silver 3

n = int(input())


def fibo_7(num):
    res = 0

    # 처음에 num+1 로 했을 때 index 범위 에러
    fibo = [0] * (num+3)

    fibo[1] = 1
    fibo[2] = 1

    for i in range(3, len(fibo)):
        # 나머지만 저장하는 방법이 핵심
        fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000007

    res = fibo[num]

    return res


print(fibo_7(n))