# Level 1

def solution(n):
    answer = 0

    q = n
    mod = ""

    while q != 0:
        mod += str(q % 3)

        q //= 3

    mod = list(map(int, mod))

    for i in range(len(mod) - 1, -1, -1):
        makeBaseTen = 3 ** (len(mod) - i - 1)
        answer += (mod[i] * makeBaseTen)

    return answer