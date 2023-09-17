# Krystal-Anne Graham

# room and directions dict
rooms = {
    'Entrance':
        {'South': 'Hallway'},
    'Hallway':
        {'North': 'Entrance', 'South': 'Study', 'East': 'Library', 'item': 'Bowl'},
    'Study':
        {'North': 'Hallway', 'item': 'Candle'},
    'Library':
        {'South': 'Fighting Hall', 'East': 'Dining Room', 'North': 'Stairwell', 'West': 'Dungeon', 'item': 'Book'},
    'Dining Room':
        {'North': 'Bedroom', 'South': 'Dungeon', 'West': 'Library', 'item': 'Salt'},
    'Bedroom':
        {'South': 'Dining Room', 'item': 'Robe'},
    'Dungeon':
        {'North': 'Dining Room'},
    'Fighting Hall':
        {'North': 'Library', 'item': 'Staff'},
    'Stairwell':
        {'South': 'Library', 'North': 'Boss Room'}
}
directions = ['North', 'South', 'East', 'West']
rooms_with_items = ['Hallway', 'Study', 'Library', 'Dining Room', 'Bedroom', 'Fighting Hall']

# defining variables
exit_command = "Exit"
item_command = "Get Item"
valid_input = directions + [exit_command] + [item_command]
invalid_input = 'Hm, that did not work! Please try: '
cannot_go_that_way = 'Oops! You see no door this way!'
game_over = 'Game Over!'
exit_room_sentinel = 'exit'
error_statement = 'Uh oh, something went wrong!'
exit_phrase = "We hope you enjoyed Annie's Adventure! Come back soon!"
item = ()
inventory = []

# instruction


# Game Start Message
game_start = """\nWelcome to Annie's Adventure! Annie Lux is an elemental witch that uses her power to keep the 
   worlds elements in balance, holding sway over the elements of fire, air, water, earth, and spirit. One 
   day, an evil wizard comes to her temple and takes her magical items, leaving her and the land in 
   disarray and the elements out of balance. Fires are starting in villages, tides are destroying towns, earthquakes are
   breaking the land, and angry spirits are harassing the country people. Annie must regain her magical items: a staff,
   a bowl, a candle, salt, and a book. Taking all 6 items, Annie must fight the evil wizard before it is too late. If 
   she doesn't, the elements may become so out of balance they destroy the world and her people.\n"""

# function to navigate rooms
def navigate(current_room: str, direction: str):
    global user_location
    user_location = rooms.get(user_location).get(user_move)
    return user_location, direction

def add_item_to_inventory(item):
    item = rooms.get(user_location).get('item')
    return item


# Initialize user location and move
user_move = None
user_location = 'Entrance'

# Giving Game Description
print(game_start)

# defining stop condition and obtaining first result


while True:
    if user_move == None:
        user_move = input('You begin in the ' + user_location + '. Begin your adventure by entering a direction: ')
    else:
        print('You are in the:', user_location)
        user_move = input('Please enter your new instruction: ')

        # starting game and checking move for valid input
        if user_move in valid_input:

            # checking for exit command
            if user_move == 'Exit':
                user_location = 'Exit'
                print(exit_phrase)
                break

            elif user_move in directions:

                if user_move in rooms.get(user_location):

                    # navigating rooms
                    result = navigate(user_location, user_move)
                    user_location = result[0]
                    #print('You are in the: ', user_location)

                    # checking to see if user in a room with an item
                    if user_location in rooms_with_items:
                        print('You see your', rooms.get(user_location).get('item'))
                        #user_move = input('Please enter a new instruction: ')

                        # if user picks up the item
                        if (user_move == item_command):
                            new_item = add_item_to_inventory(item)
                            inventory.append(new_item)
                            rooms_with_items.remove(user_location)
                            print('You have added', new_item, 'to your inventory')
                            print('Your inventory is: ', inventory)
                            #user_move = input('Please enter your new instruction: ')

                # checking for incorrect moves
                elif user_move not in rooms.get(user_location):
                    print(cannot_go_that_way)
                    #print('You are in the: ', user_location)
                    #user_move = input('Please enter a new instruction: ')

        # checking for invalid input
        elif user_move not in valid_input:
            print(invalid_input, valid_input)
            user_move = input('Please try again: ')

        # error statement if needed
        else:
            print(error_statement)
