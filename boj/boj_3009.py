# Bronze 3

xPoint = []
yPoint = []

lastX, lastY = 0, 0

for _ in range(3):
    x, y = map(int, input().split())
    
    xPoint.append(x)
    yPoint.append(y)

for i in range(3):
    if xPoint.count(x[i]) == 1:
        lastX = x[i]
    
    if yPoint.count(y[i]) == 1:
        lastY = y[i]

print(lastX, lastY)