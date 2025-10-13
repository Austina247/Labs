def initialize_board(num_rows, num_cols):
    board = []
    for i in range(num_rows):
        board.append([])
        for j in range(num_cols):
            board[i].append("-")
    return board

def print_board(board):
    count = 0
    for rows in list(board):
        print()
        count += 1
        for item in rows:
            print(item,end=" ")
    print()

def insert_chip(board, col, chip_type):
    for r in range(len(board)-1,-1,-1):
        if board[r][col] == "-":
            board[r][col] = chip_type
            break
    return r


def check_if_winner(board, col, row, chip_type):
    count = 0
    for chip in board[row]:
        if chip == chip_type:
            count += 1
        else:
            count = 0
        if count == 4:
            return True
    count = 0
    for row in board:
        if row[col] == chip_type:
            count += 1
        else:
            count = 0
        if count == 4:
            return True
    return False

rows = int(input("What would you like the height of the board to be? "))
cols = int(input("What would you like the length of the board to be? "))
board = initialize_board(rows, cols)
print_board(board)
print("\n\nPlayer 1: x\nPlayer 2: o")
win = False
player = 1
while not win:
    col = int(input(f"\nPlayer {player}: Which column would you like to choose? "))
    if player%2 == 1:
        chip_type = "x"
    else:
        chip_type = "o"
    row = insert_chip(board, col, chip_type)
    print_board(board)
    if check_if_winner(board, col, row, chip_type):
        win = True
        print(f"Player {player} won the game!")
        break
    elif board[0].count("-") == 0:
        win = True
        print("Draw. Nobody wins.")
        break

    player += 1
    if player % 2 == 1:
        player = 1

