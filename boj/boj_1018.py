# Silver 4

import sys

rows, cols = map(int, sys.stdin.readline().split())

board = [sys.stdin.readline().rstrip() for _ in range(rows)]

result = []

for row in range(rows-7):
    for col in range(cols-7):
        cnt1, cnt2 = 0, 0
        
        # 나눠진 정사각형별로 확인
        for r in range(row, row+8):
            for c in range(col, col+8):
                if (r+c)%2 == 0:
                    if board[r][c] != 'W':
                        cnt1 += 1
                    if board[r][c] != 'B':
                        cnt2 += 1
                else:
                    if board[r][c] != 'B':
                        cnt1 += 1
                    if board[r][c] != 'W':
                        cnt2 += 1
                        
        result.append(cnt1)
        result.append(cnt2)

print(min(result))