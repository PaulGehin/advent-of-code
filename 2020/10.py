def prepare_data(data, test=False):
    resu = list(map(int, data))
    resu.sort()
    resu.append(resu[-1] + 3)
    return resu


def resu1(data):
    resu = dict()
    last = 0
    for line in data:
        if line - last in resu.keys():
            resu[line - last] += 1
        else:
            resu[line - last] = 1
        last = line
    return resu[1] * resu[3]


def resu2(data):
    resu = dict()

    def resu_len(data):
        if tuple(data) in resu.keys():
            return resu[tuple(data)]
        elif len(data) == 1:
            return 1
        elif len(data) == 2:
            if data[1] - data[0] < 4:
                resu[tuple(data)] = 1
            else:
                resu[tuple(data)] = 0
        else:
            i = 1
            resu_temp = []
            while i < len(data) and data[i] - data[0] < 4:
                resu_temp.append(resu_len(data[i:]))
                i += 1
            resu[tuple(data)] = sum(resu_temp)
        return resu[tuple(data)]

    return resu_len([0] + data)


def test1(resu):
    return resu == 220


def test2(resu):
    return resu == 19208


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
