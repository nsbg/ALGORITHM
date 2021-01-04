from itertools import permutations

def prime_check(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False

    return True


def solution(numbers):
    answer = 0
    make = []

    # 모든 경우의 수 구하기
    for i in range(1, len(numbers) + 1):
        tmp = list(permutations(list(numbers), i))

        for t in tmp:
            make.append(''.join(t))

    make = list(set(map(int, make)))

    # 소수 판별
    for m in make:
        if prime_check(m):
            answer += 1

    return answer