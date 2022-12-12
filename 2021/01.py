def prepare_data(data, test=False):
    return list(map(lambda x: int(x), data))


def resu1(data):
    resu = 0
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            resu += 1
    return resu


def resu2(data):
    new_data = list()
    for i in range(len(data) - 2):
        new_data.append(data[i] + data[i + 1] + data[i + 2])
    return resu1(new_data)


def test1(resu):
    return resu == 7


def test2(resu):
    return resu == 5


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
