def prepare_data(data, test=False):
    return test, list(map(int, data))


def is_sum(resu, d):
    for i in resu:
        for j in resu:
            if i + j == d:
                return True
    return False


def resu1(data):
    test, data = data
    resu = []
    for d in data:
        if test and len(resu) < 5 or not test and len(resu) < 25:
            resu.append(d)
        elif is_sum(resu, d):
            resu.append(d)
            resu = resu[1:]
        else:
            return d
    return None


def resu2(data):
    f = resu1(data)
    data = data[1]
    for i in range(len(data) - 1):
        for j in range(2, len(data) - i):
            if sum(data[i:i + j]) == f:
                return min(data[i:i + j]) + max(data[i:i + j])
    return None


def test1(resu):
    return resu == 127


def test2(resu):
    return resu == 62


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
