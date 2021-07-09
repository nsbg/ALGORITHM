# Bronze 3

board = []

row = 0
col = 0

for i in range(9):
    num = list(map(int, input().split()))
    board.append(num)
    
m = max(board[0])

for j in range(1, len(board)):
    if m < max(board[j]):
        m = max(board[j])
        
        row = j
        col = board[j].index(max(board[j]))
        
print(m)
print(row+1, col+1)