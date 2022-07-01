
class iten:
    def __init__(self, name, attack, defense, healing):
        self.name = name
        self.atk = attack
        self.dfs =defense
        self.hlg = healing

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
    def healing(self):
        return self._healing

    @healing.setter
    def healing(self, new_healing):
        self._hp = new_healing

