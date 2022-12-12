from copy import deepcopy


def prepare_data(data, test=False):
    resu = dict()
    part1, part2 = "Part 1", "Part 2"
    resu[part1] = dict()
    resu[part2] = dict()
    for i, line in enumerate(data):
        resu[part1][i] = dict()
        resu[part2][i] = dict()
        for j, character in enumerate(line):
            resu[part1][i][j] = dict()
            resu[part1][i][j][0] = character == "#"
            resu[part2][i][j] = dict()
            resu[part2][i][j][0] = dict()
            resu[part2][i][j][0][0] = character == "#"
    return resu


def neighbors_active(cube, data):
    dim4 = len(cube) == 4
    x, y, z = cube[:3]
    if dim4:
        w = cube[3]
    resu = -1 if dim4 and data[x][y][z][w] or not dim4 and data[x][y][z] else 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if dim4:
                    for l in range(w - 1, w + 2):
                        try:
                            if data[i][j][k][l]:
                                resu += 1
                        except Exception:
                            pass
                else:
                    try:
                        if data[i][j][k]:
                            resu += 1
                    except Exception:
                        pass
    return resu


def all_cubes(data):
    x_min = min(data.keys())
    x_max = max(data.keys())
    y_min = min(data[0].keys())
    y_max = max(data[0].keys())
    z_min = min(data[0][0].keys())
    z_max = max(data[0][0].keys())
    dim4 = type(data[0][0][0]) == type(dict())
    if dim4:
        w_min = min(data[0][0][0].keys())
        w_max = max(data[0][0][0].keys())
    resu = []
    for i in range(x_min - 1, x_max + 2):
        for j in range(y_min - 1, y_max + 2):
            for k in range(z_min - 1, z_max + 2):
                if dim4:
                    for l in range(w_min - 1, w_max + 2):
                        resu.append((i, j, k, l))
                else:
                    resu.append((i, j, k))
    return resu


def compute(data):
    resu = deepcopy(data)
    cubes = all_cubes(data)
    dim4 = len(cubes[0]) == 4
    for cube in cubes:
        x, y, z = cube[:3]
        if dim4:
            w = cube[3]
        if not x in resu.keys():
            resu[x] = dict()
            data[x] = dict()
        if not y in resu[x].keys():
            resu[x][y] = dict()
            data[x][y] = dict()
        if not dim4 and not z in resu[x][y].keys():
            resu[x][y][z] = False
            data[x][y][z] = False
        elif dim4 and not z in resu[x][y].keys():
            resu[x][y][z] = dict()
            data[x][y][z] = dict()
        if dim4 and not w in resu[x][y][z].keys():
            resu[x][y][z][w] = False
            data[x][y][z][w] = False
        neighbors = neighbors_active(cube, data)
        if dim4 and data[x][y][z][w] and not neighbors in (2, 3):
            resu[x][y][z][w] = False
        elif dim4 and not data[x][y][z][w] and neighbors == 3:
            resu[x][y][z][w] = True
        elif not dim4 and data[x][y][z] and not neighbors in (2, 3):
            resu[x][y][z] = False
        elif not dim4 and not data[x][y][z] and neighbors == 3:
            resu[x][y][z] = True
    return resu


def count_active(data):
    dim4 = type(data[0][0][0]) == type(dict())
    resu = 0
    for x in data:
        for y in data[x]:
            for z in data[x][y]:
                if dim4:
                    for w in data[x][y][z]:
                        resu += int(data[x][y][z][w])
                else:
                    resu += int(data[x][y][z])
    return resu


def resu1(data):
    resu = deepcopy(data["Part 1"])
    for _ in range(6):
        resu = compute(resu)
    return count_active(resu)


def resu2(data):
    resu = deepcopy(data["Part 2"])
    for _ in range(6):
        resu = compute(resu)
    return count_active(resu)


def test1(resu):
    return resu == 112


def test2(resu):
    return resu == 848


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
