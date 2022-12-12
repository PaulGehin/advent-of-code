import math


def prepare_data(data, test=False):
    resu = dict()
    for line in data:
        locations, distance = line.split(" = ")
        resu[tuple(locations.split(" to "))] = int(distance)
    return resu


def resu1(data):
    locations = set()
    for line in data:
        for location in line:
            locations.add(location)

    def min_dist(data, went, key):
        went.add(key)
        if len(locations) == len(went):
            return 0
        else:
            resu, newkey = math.inf, key
            for line in data:
                if key in line and not line[1 - line.index(key)] in went and data[line] < resu:
                    resu, newkey = data[line], line[1 - line.index(key)]
            return resu + min_dist(data, set(went), newkey)

    return min(map(lambda key: min_dist(data, set(), key), locations))


def resu2(data):
    locations = set()
    for line in data:
        for location in line:
            locations.add(location)

    def max_dist(data, went, key):
        went.add(key)
        if len(locations) == len(went):
            return 0
        else:
            resu, newkey = 0, key
            for line in data:
                if key in line and not line[1 - line.index(key)] in went and data[line] > resu:
                    resu, newkey = data[line], line[1 - line.index(key)]
            return resu + max_dist(data, set(went), newkey)

    return max(map(lambda key: max_dist(data, set(), key), locations))


def test1(resu):
    return resu == 605


def test2(resu):
    return resu == 982


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
