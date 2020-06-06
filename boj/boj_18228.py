n = input()

a = list(map(int, input().split()))

print(min(a[:a.index(-1)])+min(a[a.index(-1)+1:]))
