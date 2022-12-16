from copy import deepcopy


def prepare_data(data, test=False):
    resu = set()
    for line in data:
        temp = None
        for coord in [x.strip() for x in line.split("->")]:
            a, b = [int(v) for v in coord.split(',')]
            if temp is not None:
                if temp[0] == a:
                    for v in range(min(temp[1], b), max(temp[1], b) + 1):
                        resu.add((a, v))
                if temp[1] == b:
                    for v in range(min(temp[0], a), max(temp[0], a) + 1):
                        resu.add((v, b))
            temp = (a, b)

    return resu


def drop(grid, void):
    x, y = 500, 0
    while y < void and not ((x, y + 1) in grid and (x - 1, y + 1) in grid and (x + 1, y + 1) in grid):
        if (x, y + 1) in grid and (x - 1, y + 1) in grid:
            x += 1
        elif (x, y + 1) in grid:
            x -= 1
        y += 1
    grid.add((x, y))
    return x, y


def resu1(data):
    grid = deepcopy(data)
    void = max(b for _, b in grid) + 1
    resu = 0
    while drop(grid, void)[1] < void:
        resu += 1
    return resu


def resu2(data):
    floor = max(b for _, b in data) + 1
    resu = 1
    while drop(data, floor) != (500, 0):
        resu += 1
    return resu


def test1(resu):
    return resu == 24


def test2(resu):
    return resu == 93


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
