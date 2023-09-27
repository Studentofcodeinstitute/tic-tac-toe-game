game_state = [None, None, None, None, None, None, None, None, None]
turn = 1


def print_board():
    global game_state
    for i in [0, 1, 2]:
        value_1 = game_state[i*3] if game_state[i*3] else " "
        value_2 = game_state[i*3+1] if game_state[i*3+1] else " "
        value_3 = game_state[i*3+2] if game_state[i*3+2] else " "
        print(f"{value_1} | {value_2} | {value_3} ")
        if i < 2:
            print(f"--|---|---")


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