game_state = [None, None, None, None, None, None, None, None, None]


def print_board():
    global game_state
    for i in [0, 1, 2]:
        value_1 = game_state[i*3] if game_state[i*3] else " "
        value_2 = game_state[i*3+1] if game_state[i*3+1] else " "
        value_3 = game_state[i*3+2] if game_state[i*3+2] else " "
        print(f"{value_1} | {value_2} | {value_3} ")
        if i < 2:
            print(f"--|---|---")


def check_win():
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [6, 3, 0], [7, 4, 1], [8, 5, 2],
            [8, 4, 0], [6, 4, 2]]
    for win in wins:
        if ((game_state[win[0]] == game_state[win[1]] == game_state[win[2]])
                and game_state[win[0]] is not None):
            print_board()
            print(game_state[win[0]] + " Won the match")
            return 1

    return -1


def take_input():
    global game_state
    while True:
        value = (input("Please enter a value between 1-9: "))
        try:
            value = int(value)
            if value < 1 or value > 9:
                print('Please type a number within the range!\n')
                return take_input()
            elif game_state[value - 1] is not None:
                print('Option also chosen earlier!\n')
                return take_input()
            else:
                return value - 1
        except ValueError:
            print("Please type a number\n")
    return value - 1


def is_game_over():
    for i in game_state:
        if i is None:
            return False

    print_board()
    return True


def main():
    global game_state
    turn = 1
    while True:
        print_board()
        if (turn == 1):
            print("X's Chance\n")
            value = take_input()
            game_state[value] = 'X'
        else:
            print("O's Chance\n")
            value = take_input()
            game_state[value] = 'O'
        has_winner = check_win()
        if (has_winner != -1):
            print("Match over\n")
            print("ATTENTION!")
            print("Any other character except 'yes' or 'y'")
            print("result in exiting the game.")
            break
        if is_game_over():
            print("Draw match\n")
            print("ATTENTION!")
            print("Any other character except 'yes' or 'y'")
            print("result in exiting the game.")
            break
        turn = 1 - turn


while True:
    print("Welcome to Tic Tac Toe game:")
    print("It is made for two players.")
    print("'X' indicate first player chance and")
    print("'O' indicate second player chance,")
    print("to win complete a straight line of your letter")
    print("(Diagonal, Horizontal, Vertical)")
    print("Positions estimated 1-9 starting at the top left.\n")
    main()
    answer = input("Do you want to play again? (Y/N): ")
    if (answer.lower() == 'y' or answer.lower() == 'yes'):
        game_state = [None, None, None, None, None, None, None, None, None]
    else:
        break
