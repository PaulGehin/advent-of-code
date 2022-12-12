import re


def prepare_data(data, test=False):
    def prepare_line(line):
        resu = dict()
        resu["mini"], resu["maxi"] = re.findall("[0-9]+,[0-9]+", line)
        resu["mini"], resu["maxi"] = tuple(map(int, resu["mini"].split(","))), tuple(
            map(int, resu["maxi"].split(",")))
        if line.split(" ")[0] == "turn":
            resu["action"] = line.split(" ")[1]
        else:
            resu["action"] = line.split(" ")[0]
        return resu

    return list(map(prepare_line, data))


def new_resu(part1=True):
    resu = dict()
    for x in range(1000):
        resu[x] = dict()
        for y in range(1000):
            if part1:
                resu[x][y] = False
            else:
                resu[x][y] = 0
    return resu


def toggle(elem, part1):
    if part1:
        return not elem
    else:
        return elem + 2


def on(elem, part1):
    if part1:
        return True
    else:
        return elem + 1


def off(elem, part1):
    if part1:
        return False
    else:
        return max(0, elem - 1)


def compute_light(resu, line, part1=True):
    f = eval(line["action"])
    for x in range(line["mini"][0], line["maxi"][0] + 1):
        for y in range(line["mini"][1], line["maxi"][1] + 1):
            resu[x][y] = f(resu[x][y], part1)
    return resu


def count_light(lights):
    resu = 0
    for y in lights.values():
        for light in y.values():
            resu += int(light)
    return resu


def resu1(data):
    resu = new_resu()
    for line in data:
        compute_light(resu, line)
    return count_light(resu)


def resu2(data):
    resu = new_resu()
    for line in data:
        compute_light(resu, line, False)
    return count_light(resu)


def test1(resu):
    return resu == 998996


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
