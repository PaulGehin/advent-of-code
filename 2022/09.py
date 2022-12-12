import re


def prepare_data(data, test=False):
    resu = [[], []]
    i = 0
    for line in data:
        m = re.match("([A-Z]+) (\\d+)", line)
        if m is not None:
            a, b = m.groups()
            resu[i].append([a, int(b)])
        else:
            i = 1
    if test:
        return resu
    return resu[0]


def resu1(data, size=2):
    if len(data) == 2:
        data = data[0]

    positions = [[0, 0] for _ in range(size)]

    visited = set()
    for a, b in data:
        for _ in range(b):
            match a:
                case "R":
                    positions[0][1] += 1
                case "L":
                    positions[0][1] -= 1
                case "U":
                    positions[0][0] += 1
                case "D":
                    positions[0][0] -= 1

            for i in range(1, len(positions)):
                positions[i] = update_pos(positions[i - 1], positions[i])

            visited.add(tuple(positions[-1]))
    return len(visited)


def update_pos(h, sec):
    t = [sec[0], sec[1]]
    if h[0] == t[0]:
        if h[1] > t[1]:
            t[1] = h[1] - 1
        elif h[1] < t[1]:
            t[1] = h[1] + 1
    elif h[1] == t[1]:
        if h[0] > t[0]:
            t[0] = h[0] - 1
        elif h[0] < t[0]:
            t[0] = h[0] + 1
    elif abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        if h[0] < t[0] and h[1] < t[1]:
            t = [t[0] - 1, t[1] - 1]
        elif h[0] < t[0] and h[1] > t[1]:
            t = [t[0] - 1, t[1] + 1]
        elif h[0] > t[0] and h[1] > t[1]:
            t = [t[0] + 1, t[1] + 1]
        else:
            t = [t[0] + 1, t[1] - 1]
    return t


def resu2(data):
    if len(data) == 2:
        data = data[1]

    return resu1(data, 10)


def test1(resu):
    return resu == 13


def test2(resu):
    return resu == 36


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
