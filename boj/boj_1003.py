# Silver 3

# f(n)은 f(0)과 f(1)을 몇 번씩 호출하는가? 로 해석 가능

t = int(input())

z = [1, 0]
o = [0, 1]

# 0, 1 호출 횟수 담은 배열 미리 생성
for i in range(2, 41):
    z.append(z[i - 1] + z[i - 2])
    o.append(o[i - 1] + o[i - 2])

for _ in range(t):
    n = int(input())

    print(z[n], o[n])