character_location = 'Entrance'
character_move = ()
inventory = []
item = ()

# rooms with items dict
item_rooms = {'Hallway': 'bowl',
              'Study': 'candle',
              'Library': 'book',
              'Fighting Hall': 'staff',
              'Dining Hall': 'Salt',
              'Bedroom': 'Robe'
              }

# function to add item to inventory
def add_item_to_inventory():
    inventory.append(item_rooms[character_location])
    print('You have added', item_rooms[character_location], 'to your inventory')
    print('Your inventory is: ', inventory)

while character_location != 'Boss Room':
    print('You are in the', character_location)
    print('Your inventory is:', inventory)
    character_move = input('Please enter your move: ')
    # entrance room
    if character_location == 'Entrance':
        if 'south' in character_move:
            character_location = 'Hallway'
        else:
            print("Can't go that way!")

    # hallway
    if character_location == 'Hallway':
        print('You are in the: ', character_location)
        if character_location in item_rooms:
            print('You see your', item_rooms[character_location])
            character_move = input('Please enter your move: ')
            if character_move == ('get bowl'):
                    add_item_to_inventory()
                    character_move = input("Please enter your move: ")
                    if 'south' in character_move:
                        character_location = 'Study'
                    elif 'north' in character_move:
                        character_location = 'Entrance'
                    else:
                        print("Can't go that way!")
            elif 'south' in character_move:
                character_location = 'Study'
            elif 'north' in character_move:
                character_location = 'Entrance'
            else:
                print("Can't go that way!")

    # study
    if character_location == 'Study':
        print('You are in the: ', character_location)
        if character_location in item_rooms:
            print('You see your', item_rooms[character_location])
            character_move = input('Please enter your move: ')
            if character_move == ('get candle'):
                    add_item_to_inventory()
                    character_move = input("Please enter your move: ")
                    if 'north' in character_move:
                        character_location = 'Hallway'
                    else:
                        print("Can't go that way!")
            elif 'north' in character_move:
                character_location = 'Hallway'
            else:
                print("Can't go that way!")

