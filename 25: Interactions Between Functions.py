from random import shuffle
example = [1, 2, 3, 4, 5, 6, 7]
def shuffle_list(my_list):
    shuffle(my_list)
    shuffle(my_list)
    shuffle(my_list)
    return my_list
def player_guess():
    player_input = ''
    while player_input not in ['0', '1', '2']:
        player_input = input("Pick a number between 0, 1 or 2")
    return int(player_input)
def check_guess(my_list, player_input):
    if my_list[player_input] == 'O':
        print('Correct!')
    else:
        print('Wrong!')
        print(f"The right answer is {my_list.index('O')}")


mylist = [' ', 'O', ' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list, guess)
