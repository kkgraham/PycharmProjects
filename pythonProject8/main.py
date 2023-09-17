# Krystal-Anne Graham

# room and directions dict
rooms = {
    'Great Hall':
        {'South': 'Bedroom'},
    'Bedroom':
        {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar':
        {'West': 'Bedroom'}
}
directions = ['North', 'South', 'East', 'West']

# defining variables
exit_command = "Exit"
valid_input = directions + [exit_command]
invalid_direction = 'Hm, that did not work! Please try: '
cannot_go_that_way = 'Oops! You see no door this way!'
game_over = 'Game Over!'
exit_room_sentinel = 'exit'
error_statement = 'Uh oh, something went wrong!'
exit_phrase = "We hope you enjoyed Annie's Adventure! Hope we see you again!"

# Game Start Message
game_start = """\nWelcome to Annie's Adventure! Annie Lux is an elemental witch that uses her power to keep the 
   worlds elements in balance, holding sway over the elements of fire, air, water, earth, and spirit. One 
   day, an evil wizard comes to her temple and takes her magical items, leaving her and the land in 
   disarray and the elements out of balance. Help Annie navigate the cave she is in and leave without 
   getting lost!\n"""


# navigate to new room using
def navigate(current_room: str, direction: str):
    global user_location
    user_location = rooms.get(user_location).get(user_move)
    direction = input('Please enter your direction: ')
    return current_room, direction


# function to create loop if invalid input is entered
def input_invalid(user_location, user_move):
    print(invalid_direction, valid_input, '.')
    print('You are in the:', user_location)
    user_move = input('Please enter your direction: ')
    return user_location, user_move


# function to quit the game from navigation function
def quit(user_location, user_move='Exit'):
    global user_location
    user_location = 'Exit'
    print('You have quit the game.')
    return user_location, user_move


# function to create a loop if in wrong move
def wrong_move(user_location, user_move):
    print(cannot_go_that_way)
    print('You are in the ', user_location)
    user_move = input('Please try a new direction: ')
    return user_location, user_move


def check_move(user_location, user_move):
    if user_move == exit_command:
        quit(user_location, user_move)
        return user_location, user_move

    elif user_move not in valid_input:
        input_invalid(user_location, user_move)
        return user_location, user_move

    elif user_move not in rooms.get(user_location):
        wrong_move(user_location, user_move)
        return user_location, user_move


# Initialize user location
user_location = 'Great Hall'

# defining stop condition and obtaining first result
user_move = input('You begin in the ' + user_location + '. Begin your adventure by entering a direction: ')

while True:

    # checking for location and moving to navigate rooms
    if (user_move in rooms.get(user_location)) and (user_move in valid_input):

        result = navigate(user_location, user_move)
        user_location = result[0]
        print('You are in the: ', user_location)
        user_move = input('Please enter a new move: ')

        if (user_move not in valid_input) or (user_move not in rooms.get(user_location)):
            new_move = check_move(user_location, user_move)
            user_move = new_move[1]
            user_location = new_move[0]

    if (user_move not in valid_input) or (user_move not in rooms.get(user_location)):
        new_move = check_move(user_location, user_move)
        user_move = new_move[1]
        user_location = new_move[0]


    # checking if Exit command is first move
    elif user_move == exit_command:
        result_exit = quit(user_location, user_move)
        break

    # continuing the game and checking next move
    else:
        print(error_statement)
        break

