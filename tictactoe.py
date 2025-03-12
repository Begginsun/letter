
board = [" " for _ in range(9)]
def draw_board():
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True
    return False


def make_move(player):
    valid_move = False
    while not valid_move:
        position = int(input(f"Игрок {player}, ходите (1-9): ")) - 1
        if 0 <= position < 9 and board[position] == " ":
            board[position] = player
            valid_move = True
        else:
            print("Неправильный ход. Попробуйте снова.")


def check_draw():
    return " " not in board

def play_game():
    draw_board()
    while True:
        make_move("X")
        draw_board()
        if check_winner("X"):
            print("X победили!")
            break
        if check_draw():
            print("Ничья!")
            break
        make_move("O")
        draw_board()
        if check_winner("O"):
            print("O победили!")
            break
        if check_draw():
            print("Ничья!")
            break

play_game()