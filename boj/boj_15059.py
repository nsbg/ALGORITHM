# Bronze 4

c1, b1, p1 = map(int, input().split())
c2, b2, p2 = map(int, input().split())

print(max(0, c2-c1)+max(0, b2-b1)+max(0, p2-p1))