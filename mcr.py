def is_win(game):
    for i in range(3):
        # Check rows and columns
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] in ['X', 'O']:
            return True
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] in ['X', 'O']:
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ['X', 'O']:
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ['X', 'O']:
        return True
    return False

def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    player1 = 'X'
    player2 = 'O'
    turn = False  # False for player 1's turn, True for player 2's turn. Player 1 first.
    print("X = Player 1")
    print("O = Player 2")
    for n in range(9):
        turn = not turn  # Switch turns
        if not turn:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Which cell to mark? i:[1..3], j:[1..3]: ")
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        if not turn:
            game[i][j] = 'X'
        else:
            game[i][j] = 'O'
        if is_win(game):
            print("Win!")
            break  # Terminate the game
        if n == 8:  # All cells have been filled
            print("Tie!")
        # Show the game board
        for row in game:
            print(" ".join(row))

if __name__ == "__main__":
    main()
