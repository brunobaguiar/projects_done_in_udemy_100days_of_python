list1 = [" ", " ", " "]
list2 = [" ", " ", " "]
list3 = [" ", " ", " "]
table = [list1, list2, list3]

is_game_over = False


def grid():
    print(" | ".join(list1))
    print("__________")
    print(" | ".join(list2))
    print("__________")
    print(" | ".join(list3))


grid()


def player1_input():
    p1_choice = input("You are X, choose the place (0,0 to 2,2): ")
    if table[int(p1_choice.split(",")[0])][int(p1_choice.split(",")[1])] == " ":
        table[int(p1_choice.split(",")[0])][int(p1_choice.split(",")[1])] = "X"
        return True
    return player1_input()


def player2_input():
    p2_choice = input("You are O, choose the place (0,0 to 2,2): ")
    if table[int(p2_choice.split(",")[0])][int(p2_choice.split(",")[1])] == " ":
        table[int(p2_choice.split(",")[0])][int(p2_choice.split(",")[1])] = "O"
        return True
    return player2_input()


def grid_full():
    for row in table:
        for item in row:
            if item == " ":
                return False
    return True


def game_rules():
    global is_game_over
    if table[0][0] == table[1][1] == table[2][2] != " "or \
            table[0][2] == table[1][1] == table[2][0] != " " or \
            table[0][0] == table[0][1] == table[0][2] != " " or \
            table[1][0] == table[1][1] == table[1][2] != " " or \
            table[2][0] == table[2][1] == table[2][2] != " " or \
            table[0][0] == table[1][0] == table[2][0] != " " or \
            table[0][1] == table[1][1] == table[2][1] != " " or \
            table[0][2] == table[1][2] == table[2][2] != " ":
        return True
    elif grid_full():
        print("It's a draw")
        is_game_over = True


def start_game():
    global is_game_over
    if not grid_full():
        if not is_game_over:
            player1_input()
            grid()
            if game_rules():
                print("X is the winner")
                is_game_over = True
        if not is_game_over:
            player2_input()
            grid()
            if game_rules():
                print("O is the winner")
                is_game_over = True
    else:
        print("It's a draw")
        is_game_over = True


while not is_game_over:
    start_game()
