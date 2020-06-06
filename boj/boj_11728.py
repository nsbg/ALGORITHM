n, m = map(int, input().split())

nmList = sorted(list(map(int, input().split())) + list(map(int, input().split())))

print(*nmList, sep=' ')


