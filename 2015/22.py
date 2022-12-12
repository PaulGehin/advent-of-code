from math import inf


class Fighter:
    def __init__(self, hp: int, damage: int = 0, defense: int = 0,
                 mana: int = 0, cost: int = 0, shield: int = 0,
                 poison: int = 0, recharge: int = 0, spent: int = 0):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.mp = mana
        self.cost = cost
        self.shield = shield
        self.poison = poison
        self.recharge = recharge
        self.spent = spent

    def __repr__(self):
        return str(self.__dict__)

    def copy(self):
        return Fighter(
            self.hp,
            self.damage,
            self.defense,
            self.mp,
            self.cost,
            self.shield,
            self.poison,
            self.recharge,
            self.spent
        )

    def tank(self, other):
        self.hp -= max(other.damage - self.defense, 0)

    def is_alive(self) -> bool:
        return self.hp > 0

    def cast_magic_missile(self, other) -> bool:
        self.mp -= 53
        self.spent += 53
        other.hp -= 4
        return self.mp >= 0

    def cast_drain(self, other) -> bool:
        self.mp -= 73
        self.spent += 73
        self.hp += 2
        other.hp -= 2
        return self.mp >= 0

    def cast_shield(self) -> bool:
        if self.shield:
            return False
        self.mp -= 113
        self.spent += 113
        self.defense += 7
        self.shield = 6
        return self.mp >= 0

    def cast_poison(self, other) -> bool:
        if other.poison:
            return False
        self.mp -= 173
        self.spent += 173
        other.poison = 6
        return self.mp >= 0

    def cast_recharge(self) -> bool:
        if self.recharge:
            return False
        self.mp -= 229
        self.spent += 229
        self.recharge = 6
        return self.mp >= 0

    def a_turn(self) -> None:
        if self.shield:
            self.shield -= 1
            if not self.shield:
                self.defense = 0
        if self.poison:
            self.hp -= 3
            self.poison -= 1
        if self.recharge:
            self.mp += 101
            self.recharge -= 1


def prepare_data(data, test=False):
    hp = data[0].split(": ")[1]
    damage = data[1].split(": ")[1]
    return Fighter(int(hp), int(damage))


def turn_boss(player: Fighter, boss: Fighter):
    player.a_turn()
    boss.a_turn()
    if boss.is_alive():
        player.tank(boss)


def fight(player: Fighter, boss: Fighter) -> (Fighter, bool):  # NOSONAR
    if not player.is_alive() or not boss.is_alive():
        return player.spent, player.is_alive()
    player.a_turn()
    boss.a_turn()
    if not player.is_alive() or not boss.is_alive():
        return player.spent, player.is_alive()
    resu = []

    player_resu = player.copy()
    boss_resu = boss.copy()
    if player_resu.cast_magic_missile(boss_resu):
        if not boss_resu.is_alive():
            resu.append(player_resu.spent)
        else:
            turn_boss(player_resu, boss_resu)
            spent_resu, win = fight(player_resu, boss_resu)
            if win:
                resu.append(spent_resu)

    player_resu = player.copy()
    boss_resu = boss.copy()
    if player_resu.cast_drain(boss_resu):
        if not boss_resu.is_alive():
            resu.append(player_resu.spent)
        else:
            turn_boss(player_resu, boss_resu)
            spent_resu, win = fight(player_resu, boss_resu)
            if win:
                resu.append(spent_resu)

    player_resu = player.copy()
    boss_resu = boss.copy()
    if player_resu.cast_shield():
        turn_boss(player_resu, boss_resu)
        spent_resu, win = fight(player_resu, boss_resu)
        if win:
            resu.append(spent_resu)

    player_resu = player.copy()
    boss_resu = boss.copy()
    if player_resu.cast_poison(boss_resu):
        turn_boss(player_resu, boss_resu)
        spent_resu, win = fight(player_resu, boss_resu)
        if win:
            resu.append(spent_resu)

    player_resu = player.copy()
    boss_resu = boss.copy()
    if player_resu.cast_recharge():
        turn_boss(player_resu, boss_resu)
        spent_resu, win = fight(player_resu, boss_resu)
        if win:
            resu.append(spent_resu)

    return min(resu, default=inf), len(resu) != 0


def resu1(boss):
    player = Fighter(50, 0, 0, 500)
    return fight(player, boss)


def resu2(boss):
    resu = 0
    return resu


def test1(resu):
    return True


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
