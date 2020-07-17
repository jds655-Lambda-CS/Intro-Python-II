from room import Room
from player import Player
from item import Item
from os import system, name


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Game:

    def __init__(self):
        # Declare all the rooms
        self.rooms = {
            'outside':  Room("Outside Cave Entrance",
                             "North of you, the cave mount beckons"),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east.""", [Item('sword', 'long sword')]),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air."""),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""", [Item('coins', '10 gold coins')]),
        }

        # Link rooms together
        self.rooms['outside'].n_to = self.rooms['foyer']
        self.rooms['foyer'].s_to = self.rooms['outside']
        self.rooms['foyer'].n_to = self.rooms['overlook']
        self.rooms['foyer'].e_to = self.rooms['narrow']
        self.rooms['overlook'].s_to = self.rooms['foyer']
        self.rooms['narrow'].w_to = self.rooms['foyer']
        self.rooms['narrow'].n_to = self.rooms['treasure']
        self.rooms['treasure'].s_to = self.rooms['narrow']

        # Make a new player object that is currently in the 'outside' room.
        self.player = Player(self.rooms['outside'])

    # define our clear function

    def start(self):
        # Main
        #

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
        playing = True
        while (playing):
            clear_screen()
            currentRoom = self.player.currentRoom

            output = f'Current room: {currentRoom.name}\n'
            # output += f'Description: {wrapper.wrap(currentRoom.description, 40)}\n\n'
            output += f'Description: {currentRoom.description}\n\n'
            output += f'Items in the room: {currentRoom.getItems()}\n'
            output += f'Items you have   : {self.player.getItems()}\n'
            output += f'Available Directions:\n{currentRoom.getConnectedRooms()}'

            availableOptions = currentRoom.getAvailableOrdinals()
            availableOptions += ', T to Take item, D to Drop item or Q to quit'
            # Print out menu
            print(output)

            #Get input for valid item, return item object
            def inputItemFrom(itemList):
                output = f'Items to Choose from:\n'
                for item in itemList:
                    output += f'\t{item.name}\n'
                selectedItem = ''
                while selectedItem not in itemList:
                    print(output)
                    selection = input('Enter selection name (or Q to quit):').upper()
                    if selection != 'Q':
                        for item in itemList:
                            if item.name.upper() == selection:
                                selectedItem = item
                    elif selection == "Q":
                        return ""

                return selectedItem

            # Run input loop until valid entry is made
            selection = ''
            def invalidSelection(selection):
                valid = (selection != 'Q') & (selection != 'N') & (selection != 'E') & (selection != 'S') & (selection != 'W')
                valid = valid & (selection != 'T') & (selection != 'D')
                return valid

            #keybord input loop
            while invalidSelection(selection):
                selection = input(f'Enter direction: {availableOptions}\n').upper()

            playing = (selection != 'Q')
            if selection == 'N':
                self.player.currentRoom = self.player.currentRoom.n_to

            elif selection == 'E':
                self.player.currentRoom = self.player.currentRoom.e_to

            elif selection == 'S':
                self.player.currentRoom = self.player.currentRoom.s_to

            if selection == 'W':
                self.player.currentRoom = self.player.currentRoom.w_to

            if selection == 'T':
                if len(currentRoom.items) != 0:
                    item = inputItemFrom(currentRoom.items)
                    if item != '':
                        self.player.items.append(item)
                        currentRoom.items.remove(item)

            if selection == 'D':
                if len(self.player.items) != 0:
                    item = inputItemFrom(self.player.items)
                    if item != '':
                        self.player.items.remove(item)
                        currentRoom.items.append(item)

