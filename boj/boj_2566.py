# Bronze 3

board = []

row = 0
col = 0

for _ in range(9):
    num = list(map(int, input().split()))
    board.append(num)
    
m = max(board[0])

for i in range(0, len(board)):
    if m <= max(board[i]):
        m = max(board[i])
        
        row = i
        col = board[i].index(m)
        
print(m)
print(row+1, col+1)