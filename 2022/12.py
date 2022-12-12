import collections
import math


def prepare_data(data, test=False):
    grid = [[v for v in line] for line in data]
    min_elevation = []
    start = end = None
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            match v:
                case "S":
                    start = (i, j)
                    min_elevation.append((i, j))
                    grid[i][j] = "a"
                case "E":
                    end = (i, j)
                    grid[i][j] = "z"
                case "a":
                    min_elevation.append((i, j))
    return [[ord(v) for v in row] for row in grid], start, end, min_elevation


def compute(grid, start, end):
    queue = collections.deque()
    queue.append((start, 0))
    seen = set()
    while queue:
        pos, n = queue.popleft()
        if pos == end:
            return n
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])
                    and grid[x + dx][y + dy] - grid[x][y] <= 1):
                queue.append(((x + dx, y + dy), n + 1))
    return math.inf


def resu1(data):
    grid, start, end, _ = data
    return compute(grid, start, end)


def resu2(data):
    grid, _, end, min_elevation = data
    return min(compute(grid, a, end) for a in min_elevation)


def test1(resu):
    return resu == 31


def test2(resu):
    return resu == 29


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
