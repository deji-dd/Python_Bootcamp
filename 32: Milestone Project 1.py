import random


def clear():
    print('\n' * 100)


def display_board(board):
    print(' - ' * 4)
    print(f'| {board[0]} '
          f'| {board[1]} '
          f'| {board[2]} |')
    print(f'| {board[3]} '
          f'| {board[4]} '
          f'| {board[5]} |')
    print(f'| {board[6]} '
          f'| {board[7]} '
          f'| {board[8]} |')
    print(' - ' * 4)


def player_input1():
    choice = ''
    while choice not in ['X', 'O']:
        choice = input("Player 1, please pick a marker (X or O): ")
        print("Please pick X or O")
    if choice == 'X':
        print("Player 1 is X, Player 2 is O")
        return 'X'
    elif choice == 'O':
        print("Player 1 is O, player 2 is X")
        return 'O'


def player_input2():
    choice = ''
    while choice not in ['X', 'O']:
        choice = input("Player 2, please pick a marker (X or O): ")
    if choice == 'X':
        print("Player 2 is X, Player 1 is O")
        return 'X'
    elif choice == 'O':
        print("Player 2 is O, player 1 is X")
        return 'O'


def place_marker(board, marker, position=0):
    while position not in range(1, 10):
        position = input("Please pick a desired number to place your marker (1-9): ")
        try:
            position = int(position)
        except ValueError:
            print("Sorry, what you chose is not a number")
    if position in range(1, 10):
        check = space_check(board, position)
        while check is True:
            print("Please pick a number that isn't already chosen.")
            position = int(input("Please pick a desired number to place your marker (1-9): "))
            check = space_check(board, position)
        if check is False:
            result = position - 1
            board[result] = marker


def win_check(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    else:
        return False


def choose_first():
    result = random.randint(1, 2)
    if result == 1:
        return "Player 1 goes first."
    else:
        return "Player 2 goes first."


def space_check(board, position):
    result = position - 1
    return type(board[result]) == str


def full_board_check(board):
    return type(board[0]) == str and type(board[1]) == str and type(board[2]) == str and type(board[3]) == str and type(board[4]) == str and type(board[5]) == str and type(board[6]) == str and type(board[7]) == str and type(board[8]) == str



def replay():
    result = ''
    while result not in ['Y', 'N']:
        result = input("Do you want to play again? (Y or N): ")
    if result == 'Y':
        return True
    elif result == 'N':
        return False


test_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Welcome to Tic Tac Toe!')
game_on = True


def number1():
    print("Here is the board: ")
    display_board(test_board)




while game_on:
    number1()
    player = choose_first()
    turn = 0
    mark1 = ''
    mark2 = ''
    if player == "Player 1 goes first.":
        mark1 = player_input1()
        if mark1 == 'X':
            mark2 = 'O'
        elif mark1 == 'O':
            mark2 = 'X'
        turn = 2
        clear()
    if player == "Player 2 goes first.":
        mark2 = player_input2()
        if mark2 == 'X':
            mark1 = 'O'
        elif mark2 == 'O':
            mark1 = 'X'
        turn = 1
        clear()
    display_board(test_board)
    while game_on:
        if turn == 2:
            print("Player 2's turn!")
            place_marker(test_board, mark2)
            clear()
            print("Here is the updated board: ")
            display_board(test_board)
            turn = 1
            win = win_check(test_board, mark2)
            draw = full_board_check(test_board)
            if win:
                print("Player 2 Wins!")
                rep = replay()
                if rep:
                    game_on = True
                    test_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    game_on = False
                    break
            if draw:
                print("It's a draw!")
                rep = replay()
                if rep:
                    game_on = True
                    test_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    game_on = False
                    break

        if turn == 1:
            print("Player 1's turn!")
            place_marker(test_board, mark1)
            clear()
            print("Here is the updated board: ")
            display_board(test_board)
            turn = 2
            win = win_check(test_board, mark1)
            draw = full_board_check(test_board)
            if win:
                print("Player 1 Wins")
                rep = replay()
                if rep:
                    game_on = True
                    test_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    clear()
                    display_board(test_board)
                else:
                    game_on = False
                    break
            if draw:
                print("It's a draw!")
                rep = replay()
                if rep:
                    game_on = True
                    test_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    clear()
                    display_board(test_board)
                else:
                    game_on = False
                    break

    break
