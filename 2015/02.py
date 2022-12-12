def prepare_data(data, test=False):
    return data


def to_int(iterable):
    return list(map(lambda x: int(x), iterable))


def wrapping_paper(box):
    l, w, h = to_int(box.split("x"))
    return 2 * l * w + 2 * w * h + 2 * h * l + min(l * w, w * h, h * l)


def ribbon(box):
    l, w, h = to_int(box.split("x"))
    return 2 * (l + w + h - max(l, w, h)) + l * w * h


def resu1(data):
    return sum(map(wrapping_paper, data))


def resu2(data):
    return sum(map(ribbon, data))


def test1(resu):
    return resu == 58 + 43


def test2(resu):
    return resu == 34 + 14


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
