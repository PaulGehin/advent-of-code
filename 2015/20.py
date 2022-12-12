import math


def prepare_data(data, test=False):
    return int(data[0])


def number_presents(house):
    yield 1
    if house != 1:
        yield house
        for i in range(2, int(math.sqrt(house)) + 1):
            if house % i == 0:
                yield i
                yield house // i


def resu1(data):
    resu = 1
    while sum(number_presents(resu)) * 10 < data:
        resu += 1
    return resu


def lazy_elves(house):
    for number in number_presents(house):
        if house // number <= 50:
            yield number


def resu2(data):
    resu = 1
    while sum(lazy_elves(resu)) * 11 < data:
        resu += 1
    return resu


def test1(resu):
    return resu == 6


def test2(resu):
    return resu == 6


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
