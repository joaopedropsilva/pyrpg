from stack import Stack
from game_constants import DEFAULT_HERO_HP, DEFAULT_HERO_DEFENSE, DEFAULT_HERO_ATK


class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = DEFAULT_HERO_HP
        self.defense = DEFAULT_HERO_DEFENSE
        self.attack = DEFAULT_HERO_ATK
        self.belt = []
        self.bag = Stack()
