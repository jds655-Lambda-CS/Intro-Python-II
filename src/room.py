# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:

    def __init__(self, name, description, items=[]):
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None
        self.name = name
        self.description = description
        self.items = items

    def getItems(self):
        itemList = ''
        for item in self.items:
            if itemList == '':
                itemList += f'{item.name}'
            else:
                itemList += f', {item.name}'
        return itemList

    def getConnectedRooms(self):
        output = ''
        if self.n_to is not None:
            output += f'\tNorth - {self.n_to.name}\n'
        if self.e_to is not None:
            output += f'\tEast - {self.e_to.name}\n'
        if self.s_to is not None:
            output += f'\tSouth - {self.s_to.name}\n'
        if self.w_to is not None:
            output += f'\tWest - {self.w_to.name}\n'
        return output


    def getAvailableOrdinals(self):
        availableOptions = ''
        if self.n_to is not None:
            availableOptions += 'N'
        if self.e_to is not None:
            if (len(availableOptions) != 0):
                availableOptions += ", "
            availableOptions += 'E'
        if self.s_to is not None:
            if (len(availableOptions) != 0):
                availableOptions += ", "
            availableOptions += 'S'
        if self.w_to is not None:
            if (len(availableOptions) != 0):
                availableOptions += ", "
            availableOptions += 'W'
        return availableOptions