def prepare_data(data, test=False):
    return data[0]


def resu1(data, init=4):
    i = init
    while len({data[k] for k in range(i - init, i)}) != init:
        i += 1
    return i


def resu2(data):
    return resu1(data, 14)


def test1(resu):
    return resu == 7


def test2(resu):
    return resu == 19


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
