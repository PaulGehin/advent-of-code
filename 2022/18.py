def prepare_data(data, test=False):
    return set(tuple(x) for x in [list(map(int, x.split(","))) for x in data])


def resu1(data):
    resu = 0
    for cube in data:
        if (cube[0] + 1, cube[1], cube[2]) not in data:
            resu += 1
        if (cube[0] - 1, cube[1], cube[2]) not in data:
            resu += 1
        if (cube[0], cube[1] + 1, cube[2]) not in data:
            resu += 1
        if (cube[0], cube[1] - 1, cube[2]) not in data:
            resu += 1
        if (cube[0], cube[1], cube[2] + 1) not in data:
            resu += 1
        if (cube[0], cube[1], cube[2] - 1) not in data:
            resu += 1
    return resu


def resu2(data):
    def legal(x):
        return -1 <= x[0] < 100 and -1 <= x[1] < 100 and -1 <= x[2] < 100 and x not in data

    outside = {(0, 0, 0)}
    pending = [(0, 0, 0)]
    while len(pending) > 0:
        cube = pending[-1]
        pending.pop()
        if (cube[0] + 1, cube[1], cube[2]) not in outside and legal((cube[0] + 1, cube[1], cube[2])):
            outside.add((cube[0] + 1, cube[1], cube[2]))
            pending.append((cube[0] + 1, cube[1], cube[2]))
        if (cube[0] - 1, cube[1], cube[2]) not in outside and legal((cube[0] - 1, cube[1], cube[2])):
            outside.add((cube[0] - 1, cube[1], cube[2]))
            pending.append((cube[0] - 1, cube[1], cube[2]))
        if (cube[0], cube[1] + 1, cube[2]) not in outside and legal((cube[0], cube[1] + 1, cube[2])):
            outside.add((cube[0], cube[1] + 1, cube[2]))
            pending.append((cube[0], cube[1] + 1, cube[2]))
        if (cube[0], cube[1] - 1, cube[2]) not in outside and legal((cube[0], cube[1] - 1, cube[2])):
            outside.add((cube[0], cube[1] - 1, cube[2]))
            pending.append((cube[0], cube[1] - 1, cube[2]))
        if (cube[0], cube[1], cube[2] + 1) not in outside and legal((cube[0], cube[1], cube[2] + 1)):
            outside.add((cube[0], cube[1], cube[2] + 1))
            pending.append((cube[0], cube[1], cube[2] + 1))
        if (cube[0], cube[1], cube[2] - 1) not in outside and legal((cube[0], cube[1], cube[2] - 1)):
            outside.add((cube[0], cube[1], cube[2] - 1))
            pending.append((cube[0], cube[1], cube[2] - 1))

    resu = 0
    for cube in data:
        if (cube[0] + 1, cube[1], cube[2]) not in data and (cube[0] + 1, cube[1], cube[2]) in outside:
            resu += 1
        if (cube[0] - 1, cube[1], cube[2]) not in data and (cube[0] - 1, cube[1], cube[2]) in outside:
            resu += 1
        if (cube[0], cube[1] + 1, cube[2]) not in data and (cube[0], cube[1] + 1, cube[2]) in outside:
            resu += 1
        if (cube[0], cube[1] - 1, cube[2]) not in data and (cube[0], cube[1] - 1, cube[2]) in outside:
            resu += 1
        if (cube[0], cube[1], cube[2] + 1) not in data and (cube[0], cube[1], cube[2] + 1) in outside:
            resu += 1
        if (cube[0], cube[1], cube[2] - 1) not in data and (cube[0], cube[1], cube[2] - 1) in outside:
            resu += 1
    return resu


def test1(resu):
    return resu == 64


def test2(resu):
    return resu == 58


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
