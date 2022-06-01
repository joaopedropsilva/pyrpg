from structures.stack import Stack


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.defense = 5
        self.attack = 5
        self.belt = []
        self.bag = Stack()
