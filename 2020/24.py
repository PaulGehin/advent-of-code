from collections import defaultdict


def prepare_data(data, test=False):
    def prepare_line(line):
        x = line.count("e") - line.count("w") - 0.5 * line.count("ne") + \
            0.5 * line.count("nw") - 0.5 * line.count("se") + \
            0.5 * line.count("sw")
        y = line.count("n") - line.count("s")
        return x, y

    return list(map(prepare_line, data))


def resu1(data):
    resu = defaultdict(bool)
    for x, y in data:
        resu[x, y] = not resu[x, y]
    return list(resu.values()).count(True)


def count_black(neighbors, data):
    resu = []
    for neighbor in neighbors:
        resu.append(data[neighbor])
    return resu.count(True)


def flip_tile(data, resu, tile, extend=False):
    x, y = tile
    neighbors = {
        (x - 0.5, y + 1),
        (x - 0.5, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x + 0.5, y + 1),
        (x + 0.5, y - 1)
    }
    for neighbor in neighbors:
        if not extend and not neighbor in resu.keys():
            flip_tile(data, resu, neighbor, True)
    number = count_black(neighbors, data)
    if data[tile]:
        resu[tile] = not (number == 0 or number > 2)
    else:
        resu[tile] = number == 2


def flip(resu):
    data = resu.copy()
    fetch = data.copy()
    for tile in data:
        flip_tile(fetch, resu, tile)


def resu2(data):
    resu = defaultdict(bool)
    for x, y in data:
        resu[x, y] = not resu[x, y]
    for _ in range(100):
        flip(resu)
    return list(resu.values()).count(True)


def test1(resu):
    return resu == 10


def test2(resu):
    return resu == 2208


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
