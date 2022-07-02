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


class Item:
    def __init__(self, name, attack, defense, healing, weight):
        self.name = name
        self.atk = attack
        self.dfs = defense
        self.hlg = healing
        self.weight = weight

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


# Items


spare_initial = Item('Lança Hereditária', 2, 0, 0, 1.05)
raw_flesh_initial = Item('Carne Crua', 0, 0, 5, 1)
sun_stone_initial = Item('Pedra do Sol', 50, 0, 100, 0.2)

iron_spare_common = Item('Lança de Ferro', 10, 0, 0, 2.25)
fruits_common = Item('Frutas', 0, 0, 5, 0.1)
grass_fork_common = Item('Forcado', 8, 0, 0, 1.25)

imperial_halberd_rare = Item('Alabarda do Exército Imperial', 25, 0, 0, 4)
meat_stew_rare = Item('Ensopado de Carne', 0, 0, 25, 0.65)

nectar_ambrosia_divine = Item('Néctar e Ambrósia', 0, 0, 50, 0.15)
sun_berserker_fists_divine = Item('Punhos do Berserker do Sol', 50, 0, 0, 0)


# Enemies

hero_daughter = Enemy('Aurora', 1, 0, 0)
deer = Enemy('Veado', 10, 0, 0)

full_moon_god = Enemy('Xaaron, Deus-Lua', 200, 100, 1000)
sun_goddess = Enemy('Hemera, Deusa-Sol', 1000, 1000, 1000)
new_moon_princess = Enemy('Nice, Princesa da Lua Nova', 40, 20, 10)
crescent_moon_prince = Enemy('Phobos, Príncipe da Lua Crescente', 75, 20, 20)
waning_moon_prince = Enemy('Deimos, Príncipe da Lua Minguante', 100, 15, 15)


all_items = {'/spare_initial': spare_initial,
             '/raw_flesh_initial': raw_flesh_initial,
             '/sun_stone_initial': sun_stone_initial,
             '/iron_spare_common': iron_spare_common,
             '/fruits_common': fruits_common,
             '/grass_fork_common': grass_fork_common,
             '/imperial_halberd_rare': imperial_halberd_rare,
             '/meat_stew_rare': meat_stew_rare,
             '/nectar_ambrosia_divine': nectar_ambrosia_divine,
             '/sun_berserker_fists_divine': sun_berserker_fists_divine}

all_enemies = {'/deer': deer,
               '/hero_daughter': hero_daughter,
               '/full_moon_god': full_moon_god,
               '/sun_goddess': sun_goddess,
               '/new_moon_princess': new_moon_princess,
               '/crescent_moon_prince': crescent_moon_prince,
               '/waning_moon_prince': waning_moon_prince}


def battle_atk(entity_one, entity_two, item_atk=0):
    entity_one_damage_given = int(entity_one.atk) + item_atk
    entity_two_total_defense = int(entity_two.hp) + int(entity_two.dfs)

    if (entity_one_damage_given >= entity_two_total_defense):
        entity_two_new_hp = 0
    else:
        entity_two_new_hp = entity_two_total_defense - entity_one_damage_given

    return entity_two_new_hp, entity_one_damage_given


def battle_healing(hp, healing_item):

    new_hp = hp + healing_item

    return new_HP


def final_battle(HP, ATK, defense, player):

    if player == 1:
        new_HP = HP - 1

    elif ATK >= HP:
        new_HP = 1
    else:
        new_HP = HP + defense - ATK
