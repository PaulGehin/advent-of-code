def prepare_data(data, test=False):
    if test:
        resu = dict()
        part = ""
        for line in data:
            if line in ("Part 1", "Part 2"):
                part = line
                resu[part] = []
            else:
                resu[part].append(line.split(" = "))
        return resu
    else:
        return list(map(lambda x: x.split(" = "), data))


def compute_bin(i, mask):
    resu = 0
    for j in range(len(mask)):
        if mask[len(mask) - j - 1] == "X":
            resu += ((i // (2 ** j)) % 2) * (2 ** j)
        else:
            resu += int(mask[len(mask) - j - 1]) * (2 ** j)
    return resu


def compute_floating(i, mask, resu=0, k=0):
    for j in range(k, len(mask)):
        if mask[len(mask) - j - 1] == "0":
            resu += ((i // (2 ** j)) % 2) * (2 ** j)
        elif mask[len(mask) - j - 1] == "1":
            resu += 2 ** j
        else:
            return compute_floating(i, mask, resu, j + 1) + compute_floating(i, mask, resu + 2 ** j, j + 1)
    return [resu]


def resu1(data):
    if type(data) == type(dict()):
        data = data["Part 1"]
    mem = dict()
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            mem[line[0].split("[")[1][:-1]] = compute_bin(int(line[1]), mask)
    resu = 0
    for key in mem:
        resu += mem[key]
    return resu


def resu2(data):
    if type(data) == type(dict()):
        data = data["Part 2"]
    mem = dict()
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for line in data:
        if line[0] == "mask":
            mask = line[1]
        else:
            for key in compute_floating(int(line[0].split("[")[1][:-1]), mask):
                mem[key] = int(line[1])
    resu = 0
    for key in mem:
        resu += mem[key]
    return resu


def test1(resu):
    return resu == 165


def test2(resu):
    return resu == 208


if __name__ == "__main__":
    import os
    import sys

    day = int(os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0])
    year = int(os.path.basename(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    from utils import run

    run(day=day, year=year, bypasstest=True)
