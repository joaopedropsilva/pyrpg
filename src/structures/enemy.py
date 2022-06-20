class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.atk = attack
        self.dfs = defense

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
