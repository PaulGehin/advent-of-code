from copy import deepcopy


def prepare_data(data, test=False):
    return list(map(lambda x: int(x), data[0].split(',')))


def compute(data, days):
    fish = [0] * 9
    for t in data:
        fish[t] += 1
    for _ in range(days):
        newborn = fish[0]
        for j in range(8):
            fish[j] = fish[j + 1]
        fish[8] = newborn
        fish[6] += newborn
    return sum(fish)


def resu1(old_data):
    return compute(deepcopy(old_data), 80)


def resu2(data):
    return compute(data, 256)


def test1(resu):
    return resu == 5934


def test2(resu):
    return resu == 26984457539


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
