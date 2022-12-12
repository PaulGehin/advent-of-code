from copy import deepcopy


def prepare_data(data, test=False):
    new_data = list()
    for line in data:
        new_data.append([int(c) for c in line])
    return new_data


def step_1(grid):
    to_flash = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
            if grid[i][j] > 9:
                to_flash.append((i, j))
    return to_flash


def step_2(grid, to_flash, flashed):
    dirs_x = [1, 1, 0, -1, -1, -1, 0, 1]
    dirs_y = [0, 1, 1, 1, 0, -1, -1, -1]

    while len(to_flash) > 0:
        (x, y) = to_flash.pop()
        flashed[x][y] = True

        for k in range(8):
            x_n = x + dirs_x[k]
            y_n = y + dirs_y[k]

            if 0 <= x_n < len(grid) and 0 <= y_n < len(grid[0]):
                grid[x_n][y_n] += 1
                if grid[x_n][y_n] == 10:
                    to_flash.append((x_n, y_n))


def step_3(grid, flashed):
    resu = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if flashed[i][j]:
                grid[i][j] = 0
                resu += 1
    return resu


def flashes(grid):
    flashed = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    to_flash = step_1(grid)
    step_2(grid, to_flash, flashed)
    return step_3(grid, flashed)


def resu1(data):
    grid = deepcopy(data)
    resu = 0
    for _ in range(100):
        resu += flashes(grid)
    return resu


def resu2(data):
    grid = deepcopy(data)
    r = 1
    while flashes(grid) != 100:
        r += 1
    return r


def test1(resu):
    return resu == 1656


def test2(resu):
    return resu == 195


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
