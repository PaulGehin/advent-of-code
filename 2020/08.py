def nop(i, accumulator, value):
    return i + 1, accumulator


def jmp(i, accumulator, value):
    return i + value, accumulator


def acc(i, accumulator, value):
    return i + 1, accumulator + value


def prepare_data(data, test=False):
    def prepare_line(line):
        x = line.split(" ")
        return (eval(x[0]), int(x[1]))

    return list(map(prepare_line, data))


def compute(data):
    accumulator, i, resu = 0, 0, set()
    while not i in resu and i < len(data):
        resu.add(i)
        key, value = data[i]
        i, accumulator = key(i, accumulator, value)
    return accumulator, i == len(data)


def resu1(data):
    return compute(data)[0]


def change_op(data, k):
    key, value = data[k]
    if key == nop:
        data[k] = (jmp, value)
        return True
    elif key == jmp:
        data[k] = (nop, value)
        return True
    else:
        return False


def resu2(data):
    def resu(k):
        if k == len(data):
            return False
        elif change_op(data, k):
            acc, value = compute(data)
            if value:
                return acc
            change_op(data, k)
        return resu(k + 1)

    return resu(0)


def test1(resu):
    return resu == 5


def test2(resu):
    return resu == 8


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
