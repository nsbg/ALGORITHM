# Silver 5
# 시간 오래 걸림

n, k = map(int, input().split())

num = sorted(list(map(int, input().split())))

print(num[k-1])