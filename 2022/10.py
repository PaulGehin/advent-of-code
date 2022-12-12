def prepare_data(data, test=False):
    cycle = 1
    x = 1
    resu = {}
    for line in data:
        match line.split():
            case ('noop', ):
                resu[cycle] = x
                cycle += 1
            case ('addx', v):
                resu[cycle] = x
                resu[cycle + 1] = x
                x += int(v)
                cycle += 2
    return resu, test


def resu1(d):
    data, _ = d
    return sum(data[i] * i for i in range(20, 221, 40))


def resu2(d):
    data, test = d
    if test:
        return None
    for i in range(1, 241):
        x = data[i]
        print('.#'[(i - 1) % 40 in (x - 1, x, x + 1)], end='')
        if i % 40 == 0:
            print()


def test1(resu):
    return resu == 13140


def test2(resu):
    return resu is None


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
