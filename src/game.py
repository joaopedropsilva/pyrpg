class LevelInfo(object):
    def __init__(self, level_code, level_number, chapter_name):
        self.level_code = level_code
        self.level_number = level_number
        self.chapter_name = chapter_name

    @property
    def level_code(self):
        return self._level_code

    @level_code.setter
    def level_code(self, new_level_code):
        self._level_code = new_level_code


class Iten:
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


def battle_ATK(HP, ATK, defense):  # nesse sistema de ataque, já conta o defalt + o item

    new_HP = HP + defense - ATK   # HP e defense são do inimigo e ATK é de quem está atacando

    return new_HP
    

def battle_healing(HP, healing_iten):

    new_HP = HP + healing_iten

    return new_HP