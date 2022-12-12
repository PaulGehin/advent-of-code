from math import prod


def prepare_data(data, test=False):
    resu = []
    for i, line in enumerate(data):
        resu.append([])
        for elem in line:
            if elem == ".":
                resu[i].append(False)
            elif elem == "#":
                resu[i].append(True)
    return resu


def slide(data, value):
    resu, x, y = 0, 0, 0
    a, b = value
    height, width = len(data), len(data[0])
    while y < height:
        if data[y][x % width]:
            resu += 1
        x += a
        y += b
    return resu


def resu1(data):
    return slide(data, (3, 1))


def resu2(data):
    possibilities = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return prod(map(lambda x: slide(data, x), possibilities))


def test1(resu):
    return resu == 7


def test2(resu):
    return resu == 336


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
