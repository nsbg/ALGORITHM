n, m = map(int, input().split())

nx = (n-1) // 4
ny = (n-1) % 4

mx = (m-1) // 4
my = (m-1) % 4

print(abs(mx-nx)+abs(my-ny))
