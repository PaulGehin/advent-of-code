from collections import deque, defaultdict


def prepare_data(data, test=False):
    new_data = defaultdict(set)
    for line in data:
        line = line.strip().split("-")
        new_data[line[0]].add(line[1])
        new_data[line[1]].add(line[0])
    return new_data


def resu1(data, is_part_1=True):
    paths = deque()
    resu = 0
    paths.append((0, "start", ["start"], False))
    while paths:
        steps, position, path, small_cave_visited = paths.popleft()
        if position == "end":
            resu += 1
            continue
        for node in data[position]:
            if node.islower() and node in path:
                if node == "start" or small_cave_visited or is_part_1:
                    continue
                else:
                    paths.append((steps + 1, node, path + [node], True))
            else:
                paths.append((steps + 1,
                              node,
                              path + [node],
                              small_cave_visited))
    return resu


def resu2(data):
    return resu1(data, False)


def test1(resu):
    return resu == 226


def test2(resu):
    return resu == 3509


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
