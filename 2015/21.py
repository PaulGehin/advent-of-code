from math import inf


class Fighter:
    def __init__(self, hp: int, damage: int = 0, defense: int = 0):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.cost = 0

    def __repr__(self):
        return str(self.__dict__)

    def copy(self):
        return Fighter(self.hp, self.damage, self.defense)

    def tank(self, other):
        self.hp -= max(other.damage - self.defense, 0)

    def is_alive(self) -> bool:
        return self.hp > 0

    def equip(self, weapon, armor, rings):
        cost, damage = weapon
        self.cost += cost
        self.damage = damage
        cost, defense = armor
        self.cost += cost
        self.defense = defense
        for cost, ring in rings:
            self.cost += cost
            damage, defense = ring
            self.damage += damage
            self.defense += defense


def fight(player: Fighter, boss: Fighter):
    while boss.is_alive() and player.is_alive():
        boss.tank(player)
        player.tank(boss)
    return not boss.is_alive()


def buy_weapons():
    resu = []
    resu.append((8, 4))
    resu.append((10, 5))
    resu.append((25, 6))
    resu.append((40, 7))
    resu.append((74, 8))
    return resu


def buy_armors():
    resu = []
    resu.append((0, 0))
    resu.append((13, 1))
    resu.append((31, 2))
    resu.append((53, 3))
    resu.append((75, 4))
    resu.append((102, 5))
    return resu


def buy_rings():
    rings = []
    rings.append((25, (1, 0)))
    rings.append((50, (2, 0)))
    rings.append((100, (3, 0)))
    rings.append((20, (0, 1)))
    rings.append((40, (0, 2)))
    rings.append((80, (0, 3)))
    resu = []
    resu.append([])
    for ring in rings:
        resu.append([ring])
    for ring_1 in rings:
        for ring_2 in rings:
            if ring_1 != ring_2:
                resu.append([ring_1, ring_2])
    return resu


def prepare_data(data, test=False):
    hp = data[0].split(": ")[1]
    damage = data[1].split(": ")[1]
    armor = data[2].split(": ")[1]
    return Fighter(int(hp), int(damage), int(armor))


def resu1(boss):
    resu = inf
    for weapon in buy_weapons():
        for armor in buy_armors():
            for rings in buy_rings():
                player = Fighter(100)
                player.equip(weapon, armor, rings)
                if player.cost < resu and fight(player, boss.copy()):
                    resu = player.cost
    return resu


def resu2(boss):
    resu = 0
    for weapon in buy_weapons():
        for armor in buy_armors():
            for rings in buy_rings():
                player = Fighter(100)
                player.equip(weapon, armor, rings)
                if player.cost > resu and not fight(player, boss.copy()):
                    resu = player.cost
    return resu


def test1(resu):
    return resu == 8


def test2(resu):
    return resu == 0


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
