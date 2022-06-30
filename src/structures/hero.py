from structures.stack import Stack


class Hero:
    def __init__(self, name, hp, attack, defense, screen_count):
        self.name = name
        self.hp = hp
        self.atk = attack
        self.dfs = defense
        self.belt = []
        self.bag = Stack()
        self.screens = screen_count

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, new_hp):
        self._hp = new_hp

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, new_atk):
        self._atk = new_atk

    @property
    def dfs(self):
        return self._dfs

    @dfs.setter
    def dfs(self, new_dfs):
        self._dfs = new_dfs

    @property
    def screens(self):
        return self._screens

    @screens.setter
    def screens(self, new_screens):
        self._screens = new_screens
