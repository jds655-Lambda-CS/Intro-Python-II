# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, startingRoom: Room, items=[]):
        self.currentRoom = startingRoom
        self.items = items

    def getItems(self):
        itemList = ''
        for item in self.items:
            if itemList == '':
                itemList += f'{item.name}'
            else:
                itemList += f', {item.name}'
        return itemList

