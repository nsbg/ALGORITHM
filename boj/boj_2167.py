# n : 세로 줄, m : 가로 줄
n, m = map(int, input().split())

numList = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

for _ in range(k):
