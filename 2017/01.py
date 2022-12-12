def prepare_data(data, test=False):
    if test:
        return [int(x) for x in data[0]], [int(x) for x in data[1]]
    return [int(x) for x in data[0]]


def resu1(data, gap=1):
    if len(data) == 2:
        data = data[0]
    resu = []
    for i, d in enumerate(data):
        if d == data[(i + gap) % len(data)]:
            resu.append(d)
    return sum(resu)


def resu2(data):
    if len(data) == 2:
        data = data[1]
    return resu1(data, len(data) // 2)


def test1(resu):
    return resu == 9


def test2(resu):
    return resu == 4


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
