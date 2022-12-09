board = input()

i = 0
while True:
    if i == len(board):
        break
    if board[i:i+4] == 'XXXX':
        i = i + 4
        board = board.replace('X','A', 4)
    elif board[i:i+2] == 'XX':
        i = i + 2
        board = board.replace('X','B',2)
    elif board[i] == '.':
        i = i + 1
    else:
        board =-1
        break
print(board)