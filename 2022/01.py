def prepare_data(data, test=False):
    return [sum(int(food) for food in elf.split("\n")) for elf in ("\n".join(data)).split("\n\n")]


def resu1(data):
    return max(data)


def resu2(data):
    data.sort()
    return sum(data[-3:])


def test1(resu):
    return resu == 24000


def test2(resu):
    return resu == 45000


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
