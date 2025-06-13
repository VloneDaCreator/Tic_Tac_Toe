board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    print("   0   1   2")
    print("  -----------")
    print("0| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2]))
    print("  -----------")
    print("1| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2]))
    print("  -----------")
    print("2| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2]))
    print("  -----------")

def check_winner(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_board_full():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


players = ["X", "O"]
current_player = 0

while True:
    print_board()
    move = input("Player " + players[current_player] + ", enter your move (row and column): ")
    move = move.split()
    row = int(move[0])
    col = int(move[1])

    if board[row][col] != " ":
        print("Invalid move! Cell already taken. Try again.")
        continue

    board[row][col] = players[current_player]
    
    if check_winner(players[current_player]):
        print("Player " + players[current_player] + " wins!")
        break
    if is_board_full():
        print("It's a draw!")
        break
    current_player = (current_player + 1) % 2