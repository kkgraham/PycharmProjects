# Krystal-Anne Graham
# test comment


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
        {'South': 'Library', 'North': 'Boss Room'},
    'Boss Room':
        'Exit'
}
directions = ['North', 'South', 'East', 'West']

item_room_list = ['Hallway', 'Study', 'Library', 'Dining Room', 'Bedroom', 'Fighting Hall']

# defining variables
user_location = ()
user_move = ()
exit_command = "Exit"
item_command = "Get Item"
valid_input = directions + [exit_command] + [item_command]
invalid_input = 'Hm, that did not work! Please try: '
cannot_go_that_way = 'Oops! You see no door this way!'
game_over = '************Game Over!!************'
lose_phrase = "Annie doesn't have all her items! Agahnim is too strong!\n"
win_phrase = """Annie has all 6 of her magical items! She is stronger than Agahnim!
                            You win!
                You helped Annie save the world!"""
error_statement = 'Uh oh, something went wrong!'
exit_phrase = "We hope you enjoyed Annie's Adventure! Come back soon!"
room_item = ()
inventory = []


# function to relay instructions
def show_instructions():
    instructions = """Welcome to Annie's Adventure! Annie Lux is an elemental witch that uses her power to keep the 
   world's elements in balance, holding sway over the elements of fire, air, water, earth, and spirit. One 
   day, an evil wizard named Agahnim comes to her temple and takes her magical items, leaving her and the land in 
   disarray and the elements out of balance. Fires are starting in villages, tides are destroying towns, earthquakes are
   breaking the land, and angry spirits are harassing the country people. Annie must regain her magical items: a staff,
   a bowl, a candle, salt, and a book. Taking all 6 items, Annie must fight Agahnim before it is too late. If 
   she doesn't, the elements may become so out of balance they destroy the world and her people. Help Annie collect the 
   items she needs to defeat the evil wizard!
   
   In this game, you can enter your moves. You can enter: North, South, East, West, Get Item, and Exit.
   Using a direction move will move Annie in that direction, if it is available.
   Using "Get Item" will add the item to your inventory if there is an item in the room.
   Using "Exit" will quit the game.
   
   Your goal is to collect all 6 items in the dungeon before facing Agahnim. If you face him without all 6 items, Annie
   will lose her fight, and it will be game over.
   """

    print(instructions)


# function to start game
def start_game(location, instruction):
    global user_location
    global user_move
    user_location = 'Entrance'
    user_move = input('You begin in the Entrance. Please enter your first instruction: ')
    return user_location, user_move


# function to navigate rooms
def navigate(current_room: str, direction: str):
    global user_location
    user_location = rooms.get(user_location).get(user_move)
    return user_location, direction


# function to add item to inventory
def add_item():
    global room_item
    global inventory
    inventory.append(rooms.get(user_location).get('item'))
    item_room_list.remove(user_location)
    return inventory


# main function
def main():
    global user_location
    global user_move
    global inventory

    while True:
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

                    # user reaches boss room
                    if user_location == 'Boss Room':
                        print('You are in the: ', user_location)
                        print('Your inventory is: ', inventory)
                        print('--------------------------')
                        print('Agahnim is here!')

                        # game over, not all items
                        if (len(inventory) < 6):
                            print(lose_phrase)
                            print(game_over)
                            print(exit_phrase)
                            break

                        # game won
                        elif (len(inventory) == 6):
                            print(win_phrase)
                            print(exit_phrase)
                            break

                    # allowing to get item
                    elif user_location in item_room_list:
                        print('You are in the: ', user_location)
                        print('Your inventory is: ', inventory)
                        print('You see your', rooms.get(user_location).get('item'))
                        print('--------------------------')
                        user_move = input('Please enter a new instruction: ')

                        if user_move == item_command:
                            inventory = add_item()
                            print('You have added the item to your inventory.')
                            print('Inventory: ', inventory)
                            print('You are in the: ', user_location)
                            print('--------------------------')
                            user_move = input('Please enter a new instruction: ')

                    elif user_location not in item_room_list:
                        print('You are in the: ', user_location)
                        print('Your inventory is: ', inventory)
                        print('--------------------------')
                        user_move = input('Please enter a new instruction: ')

                # checking for incorrect moves
                elif user_move not in rooms.get(user_location):
                    print(cannot_go_that_way)
                    print('You are in the: ', user_location)
                    print('--------------------------')
                    user_move = input('Please enter a new instruction: ')

        # checking for invalid input
        elif user_move not in valid_input:
            print(invalid_input, valid_input)
            print('--------------------------')
            user_move = input('Please try again: ')

        # error statement if needed
        else:
            print(error_statement)


# Execute Game
show_instructions()
result = start_game(user_location, user_move)
user_location = result[0]
user_move = result[1]
main()
