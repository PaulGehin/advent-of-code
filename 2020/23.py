from copy import deepcopy
from itertools import islice
from math import prod


def prepare_data(data, test=False):
    return list(map(int, data[0]))


class Node:
    def __init__(self, val):
        self.val = val


def cup_game(numbers, moves):
    cups = [Node(i) for i in numbers]
    for cup, cup_r in zip(cups, cups[1:] + [cups[0]]):
        cup.right = cup_r
    lookup = {cup.val: cup for cup in cups}

    cup = cups[0]
    n = len(numbers)

    def decrement(x):
        return n if x == 1 else x - 1

    for _ in range(moves):
        val = decrement(cup.val)
        cup.right = (cup_rrr := (cup_rr := (
            cup_r := cup.right).right).right).right
        while val in {cup_r.val, cup_rr.val, cup_rrr.val}:
            val = decrement(val)
        dest = lookup[val]
        dest.right, cup_rrr.right, cup = cup_r, dest.right, cup.right

    cup = lookup[1]
    while (cup := cup.right):
        yield cup.val


def resu1(data):
    digits = deepcopy(data)
    moves = 100
    return int(''.join(map(str, islice(cup_game(digits, moves), len(digits) - 1))))


def resu2(data):
    numbers = deepcopy(data) + list(range(max(data) + 1, 1000000 + 1))
    moves = 10000000
    return prod(islice(cup_game(numbers, moves), 2))


def test1(resu):
    return resu == 67384529


def test2(resu):
    return resu == 149245887792


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
