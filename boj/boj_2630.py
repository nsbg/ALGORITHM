# Silver 2

import sys

white, blue = 0, 0

def recursive(x, y, n):
    one_color = 0
    
    global white
    global blue
            
    for i in range(x, x+n):
        for j in range(y, y+n):
            if int(paper[i][j]) == 1:
                one_color += 1
    
    if one_color == n*n:
        blue += 1
    elif one_color == 0:
        white += 1
    else:
        recursive(x, y, n//2)
        recursive(x+n//2, y, n//2)
        recursive(x, y+n//2, n//2)
        recursive(x+n//2, y+n//2, n//2)

N = int(input())

paper = [sys.stdin.readline().split() for _ in range(N)]

recursive(0, 0, N)

print(white, blue, sep='\n')