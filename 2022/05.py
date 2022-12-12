import re
from copy import deepcopy


def prepare_data(data, test=False):
    stacks = []
    moves = []
    for row in data:
        if row.strip().startswith("1"):
            break
        for i, val in enumerate(row):
            if 'A' <= val <= 'Z':
                i = int((i - 1) / 4)
                while len(stacks) <= i:
                    stacks.append([])
                stacks[i].append(val)
    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]

    for row in [x.lstrip(".") for x in data]:
        m = re.search("move ([0-9]+) from ([0-9]+) to ([0-9]+)", row)
        if m is not None:
            moves.append(tuple(map(int, m.groups())))
    return {
        "stacks": stacks,
        "moves": moves
    }


def resu1(data):
    stacks = deepcopy(data["stacks"])
    moves = deepcopy(data["moves"])
    for a, b, c in moves:
        for _ in range(a):
            stacks[c - 1].append(stacks[b - 1].pop())

    resu = ""
    for stack in stacks:
        resu += stack.pop()
    return resu


def resu2(data):
    stacks = deepcopy(data["stacks"])
    moves = deepcopy(data["moves"])
    for a, b, c in moves:
        temp = []
        for _ in range(a):
            temp.append(stacks[b - 1].pop())
        stacks[c - 1] += temp[::-1]

    resu = ""
    for stack in stacks:
        resu += stack.pop()
    return resu


def test1(resu):
    return resu == "CMZ"


def test2(resu):
    return resu == "MCD"


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
