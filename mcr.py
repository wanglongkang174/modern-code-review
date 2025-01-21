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
    game = [[' ' for _ in range(3)] for _ in range(3)]  # 初始化井字棋棋盘
    player1 = 'X'
    player2 = 'O'
    print("欢迎来到井字棋游戏！")
    print("Player 1 是 'X'")
    print("Player 2 是 'O'")
    print("游戏开始：")

    for turn in range(9):
        current_player = player1 if turn % 2 == 0 else player2
        print(f"\n轮到 Player {1 if current_player == 'X' else 2} ({current_player}) 下棋！")
        i, j = get_valid_input(game)  # 获取有效输入
        game[i][j] = current_player

        # 显示当前棋盘
        print("\n当前棋盘：")
        for row in game:
            print(" | ".join(row))
            print("-" * 9)

        # 检查是否胜利
        if is_win(game):
            print(f"Player {1 if current_player == 'X' else 2} ({current_player}) 赢了！")
            break
    else:
        print("游戏平局！")

if __name__ == "__main__":
    main()
