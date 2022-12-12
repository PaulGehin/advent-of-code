def prepare_data(data, test=False):
    return data[0]


def floor_by_parenthesis(character):
    if character == "(":
        return 1
    elif character == ")":
        return -1
    else:
        raise Exception()


def resu1(data):
    return sum(map(floor_by_parenthesis, data))


def resu2(data):
    resu = 1
    while sum(map(floor_by_parenthesis, data[:resu])) != -1:
        resu += 1
    return resu


def test1(resu):
    return resu == -3


def test2(resu):
    return resu == 1


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
