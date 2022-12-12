import re
from dataclasses import dataclass


@dataclass
class Teaspoon:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def prepare_data(data, test=False):
    parser = re.compile(
        r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
    )

    def prepare_line(line):
        match = re.search(parser, line)
        if not match:
            raise ValueError("Can't parse line")
        name, capacity, durability, flavor, texture, calories = \
            match.group(1, 2, 3, 4, 5, 6)
        return Teaspoon(name, int(capacity), int(durability),
                        int(flavor), int(texture), int(calories))

    return list(map(prepare_line, data))


def find(ingredients, indice, amounts, volume, calories, max_score_seen):
    if len(ingredients) - 1 == indice:
        amounts.append(volume)
        cap = sum(
            amounts[a] * ingredients[a].capacity for a in range(indice + 1))
        dur = sum(
            amounts[a] * ingredients[a].durability for a in range(indice + 1))
        fla = sum(
            amounts[a] * ingredients[a].flavor for a in range(indice + 1))
        tex = sum(
            amounts[a] * ingredients[a].texture for a in range(indice + 1))

        cap = max(0, cap)
        dur = max(0, dur)
        fla = max(0, fla)
        tex = max(0, tex)

        if calories is not None:
            cals = sum(
                amounts[a] * ingredients[a].calories for a in range(indice + 1))
            if cals != calories:
                return max_score_seen

        this_score = cap * dur * fla * tex
        return max(max_score_seen, this_score)
    else:
        for i in range(0, volume + 1):
            max_score_seen = find(
                ingredients, indice + 1,
                             amounts + [i], volume - i,
                calories, max_score_seen)
        return max_score_seen


def resu1(data):
    return find(data, 0, [], 100, None, 0)


def resu2(data):
    return find(data, 0, [], 100, 500, 0)


def test1(resu):
    return True


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
