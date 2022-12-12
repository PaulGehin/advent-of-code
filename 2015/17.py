from copy import deepcopy
from math import inf


def prepare_data(data, test=False):
    resu = list(map(int, data))
    target = 25 if test else 150
    return list(fill(resu, target))


def fill(containers, target):
    if len(containers) == 1 and containers[0] == target:
        yield containers
    elif len(containers) != 1:
        for i, container in enumerate(containers):
            if container > target:
                continue
            elif container == target:
                yield [container]
            else:
                data = deepcopy(containers)[i + 1:]
                for resu in fill(data, target - container):
                    yield [container] + resu


def resu1(data):
    return len(data)


def resu2(data):
    number = inf
    for way in data:
        if len(way) < number:
            number, resu = len(way), 1
        elif len(way) == number:
            resu += 1
    return resu


def test1(resu):
    return resu == 4


def test2(resu):
    return resu == 3


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
