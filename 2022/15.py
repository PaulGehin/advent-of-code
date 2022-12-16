import re

import numpy as np
from scipy.spatial.distance import cityblock
from tqdm import tqdm


def prepare_data(data, test=False):
    resu = list()
    for line in data:
        m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line)
        s_x, s_y, b_x, b_y = map(int, m.groups())
        resu.append(((s_x, s_y), (b_x, b_y), cityblock((s_x, s_y), (b_x, b_y))))
    return resu, test


def resu1(data):
    data, test = data
    y = 10 if test else 2_000_000

    max_d = max([distance for _, _, distance in data])
    min_x = min(min(s[0], b[0]) for s, b, _ in data)
    max_x = max(max(s[0], b[0]) for s, b, _ in data)

    resu = 0
    for x in tqdm(range(min_x - max_d - 10, max_x + max_d + 10), disable=test):
        for sensor, beacon, distance in data:
            if beacon == (x, y):
                break
            if abs(sensor[0] - x) + abs(sensor[1] - y) <= distance:
                resu += 1
                break

    return resu


def resu2(data):
    data, test = data

    max_x_y = 20 if test else 4_000_000
    for y in tqdm(range(max_x_y + 1), disable=test):
        x = 0
        while x <= max_x_y:
            for sensor, beacon, distance in data:
                if beacon == (x, y):
                    break
                if abs(sensor[0] - x) + abs(sensor[1] - y) <= distance:
                    new_x = sensor[0] + distance - abs(sensor[1] - y)
                    if new_x != x:
                        x = new_x - 1
                    break
            else:
                return np.ulonglong(x) * np.ulonglong(4_000_000) + np.ulonglong(y)
            x += 1


def test1(resu):
    return resu == 26


def test2(resu):
    return resu == 56000011


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
