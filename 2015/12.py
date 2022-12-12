import json


def prepare_data(data, test=False):
    return json.loads(data[0])


def find_numbers(data):
    resu = []
    if type(data) == type(int()):
        resu.append(int(data))
    elif type(data) == type(dict()):
        for key in data:
            resu += find_numbers(data[key]) + find_numbers(key)
    elif type(data) == type(list()):
        for value in data:
            resu += find_numbers(value)
    return resu


def find_numbers(data, count_red=True):
    resu = []
    if type(data) == type(int()):
        resu.append(int(data))
    elif type(data) == type(dict()):
        if count_red or not "red" in data.values():
            for key in data:
                resu += find_numbers(data[key], count_red) + \
                        find_numbers(key, count_red)
    elif type(data) == type(list()):
        for value in data:
            resu += find_numbers(value, count_red)
    return resu


def resu1(data):
    return sum(find_numbers(data))


def resu2(data):
    return sum(find_numbers(data, False))


def test1(resu):
    return resu == 0


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
