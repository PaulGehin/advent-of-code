def prepare_data(data, test=False):
    return list(map(int, data))


def transform(x, s):
    return pow(x, s, 20201227)


def resu1(data):
    door_key, card_key = data

    loop_size = 0
    while transform(7, loop_size) != card_key:
        loop_size += 1

    return transform(door_key, loop_size)


def resu2(data):
    return "Nothingness"


def test1(resu):
    return resu == 14897079


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
