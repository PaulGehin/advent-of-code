from collections import deque
from math import prod


def prepare_data(data, test=False):
    new_data = list()
    for line in data:
        new_data.append(list(map(lambda x: int(x), [c for c in line])))
    return new_data


def is_low_point(i, j, data):
    a, b = False, False
    if i == 0:
        a = data[i][j] < data[i + 1][j]
    elif i == len(data) - 1:
        a = data[i][j] < data[i - 1][j]
    else:
        a = data[i][j] < data[i - 1][j] and data[i][j] < data[i + 1][j]
    if j == 0:
        b = data[i][j] < data[i][j + 1]
    elif j == len(data[0]) - 1:
        b = data[i][j] < data[i][j - 1]
    else:
        b = data[i][j] < data[i][j - 1] and data[i][j] < data[i][j + 1]
    return a and b


def resu1(data):
    low_points = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_low_point(i, j, data):
                low_points.append(data[i][j] + 1)
    return sum(low_points)


def resu2(data):
    wide = len(data)
    height = len(data[0])
    offset_x = [-1, 0, 1, 0]
    offset_y = [0, 1, 0, -1]
    sizes = []
    seen = set()
    for i in range(wide):
        for j in range(height):
            if (i, j) not in seen and data[i][j] != 9:
                size = 0
                turtle = deque()
                turtle.append((i, j))
                while turtle:
                    (i, j) = turtle.popleft()
                    if (i, j) in seen:
                        continue
                    seen.add((i, j))
                    size += 1
                    for k in range(4):
                        x = i + offset_x[k]
                        y = j + offset_y[k]
                        if 0 <= x < wide and 0 <= y < height and data[x][y] != 9:
                            turtle.append((x, y))
                sizes.append(size)
    sizes.sort()
    return prod(sizes[-3:])


def test1(resu):
    return resu == 15


def test2(resu):
    return resu == 1134


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
