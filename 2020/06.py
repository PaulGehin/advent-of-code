def prepare_data(data, test=False):
    resu = [[]]
    i = 0
    for line in data:
        if line == "":
            resu.append([])
            i += 1
        else:
            resu[i].append(set(line))
    return resu


def resu1(data):
    return sum(map(lambda group: len(set().union(*group)), data))


def resu2(data):
    return sum(map(lambda group: len(group.pop().intersection(*group)), data))


def test1(resu):
    return resu == 11


def test2(resu):
    return resu == 6


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
