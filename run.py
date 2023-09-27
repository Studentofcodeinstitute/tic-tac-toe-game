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