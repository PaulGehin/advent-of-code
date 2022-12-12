def prepare_data(data, test=False):
    return list(map(lambda x: int(x), data))


def resu1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j


def resu2(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i * j * k


def test1(resu):
    return resu == 514579


def test2(resu):
    return resu == 241861950


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
