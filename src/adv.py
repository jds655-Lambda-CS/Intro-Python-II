from room import Room
from player import Player
from textwrap import TextWrapper
import os

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
wrapper = TextWrapper()
playing = True
while (playing):
    currentRoom = player.currentRoom
    availableOptions = ''
    output = f'Current room: {currentRoom.name}\n'
    # output += f'Description: {wrapper.wrap(currentRoom.description, 40)}\n\n'
    output += f'Description: {currentRoom.description}\n\n'
    output += f'Available Directions:\n'
    if currentRoom.n_to is not None:
        output += f'\tNorth - {currentRoom.n_to.name}\n'
        availableOptions += 'N'

    if currentRoom.e_to is not None:
        output += f'\tEast - {currentRoom.e_to.name}\n'
        if (len(availableOptions) != 0):
            availableOptions += ", "
        availableOptions += 'E'

    if currentRoom.s_to is not None:
        output += f'\tSouth - {currentRoom.s_to.name}\n'
        if (len(availableOptions) != 0):
            availableOptions += ", "
        availableOptions += 'S'

    if currentRoom.w_to is not None:
        output += f'\tWest - {currentRoom.w_to.name}\n'
        if (len(availableOptions) != 0):
            availableOptions += ", "
        availableOptions += 'W'

    availableOptions += ', or Q to quit'

    print(output)
    selection = ''
    while (selection != 'Q') & (selection != 'N') & (selection != 'E') & (selection != 'S') & (selection != 'W'):
        selection = input(f'Enter direction: {availableOptions}\n').upper()
    playing = (selection != 'Q')
    if selection == 'N':
        player.currentRoom = player.currentRoom.n_to

    if selection == 'E':
        player.currentRoom = player.currentRoom.e_to

    if selection == 'S':
        player.currentRoom = player.currentRoom.s_to

    if selection == 'W':
        player.currentRoom = player.currentRoom.w_to
    os.system('cls')