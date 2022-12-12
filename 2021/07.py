def prepare_data(data, test=False):
    return list(map(lambda x: int(x), data[0].split(',')))


def resu1(data):
    return min([sum([abs(x - i) for x in data]) for i in range(min(data), max(data) + 1)])


def resu2(data):
    return min([sum([abs(x - i) * (abs(x - i) + 1) // 2 for x in data]) for i in range(min(data), max(data) + 1)])


def test1(resu):
    return resu == 37


def test2(resu):
    return resu == 168


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
