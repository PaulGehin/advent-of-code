import heapq
from copy import deepcopy


def prepare_data(data, test=False):
    return [[int(c) for c in line.strip()] for line in data]


def process(dist, position, target):
    if position == target:
        return dist
    else:
        return None


def compute(start, neighbors_fn, target):
    to_search = [(0, start)]
    heapq.heapify(to_search)
    seen = set()
    while len(to_search) > 0:
        dist, position = heapq.heappop(to_search)
        if position in seen:
            continue
        seen.add(position)
        result = process(dist, position, target)
        if result is not None:
            return result
        for step, neighbor in neighbors_fn(position):
            heapq.heappush(to_search, (dist + step, neighbor))
    return None


def resu1(old_data):
    data = deepcopy(old_data)

    def neighbors(position):
        x, y = position
        resu = []
        if x > 0:
            resu.append((data[y][x - 1], (x - 1, y)))
        if x < len(data[y]) - 1:
            resu.append((data[y][x + 1], (x + 1, y)))
        if y > 0:
            resu.append((data[y - 1][x], (x, y - 1)))
        if y < len(data) - 1:
            resu.append((data[y + 1][x], (x, y + 1)))
        return resu

    return compute((0, 0), neighbors, (len(data[0]) - 1, len(data) - 1))


def resu2(data):
    repeats = 5

    def risk(x, y):
        big_x = x // len(data[0])
        small_x = x % len(data[0])
        big_y = y // len(data)
        small_y = y % len(data)
        return (data[small_y][small_x] + big_x + big_y - 1) % 9 + 1

    def neighbors(position):
        x, y = position
        resu = []
        if x > 0:
            resu.append((risk(x - 1, y), (x - 1, y)))
        if x < len(data[0]) * repeats - 1:
            resu.append((risk(x + 1, y), (x + 1, y)))
        if y > 0:
            resu.append((risk(x, y - 1), (x, y - 1)))
        if y < len(data) * repeats - 1:
            resu.append((risk(x, y + 1), (x, y + 1)))
        return resu

    return compute((0, 0), neighbors, (len(data[0]) * repeats - 1, len(data) * repeats - 1))


def test1(resu):
    return resu == 40


def test2(resu):
    return resu == 315


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
