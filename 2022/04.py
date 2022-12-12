def prepare_data(data, test=False):
    def prepare_line(line):
        a, b = line.split(',')
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')
        return (int(a1), int(a2)), (int(b1), int(b2))

    return [prepare_line(line) for line in data]


def resu1(data):
    def f(a, b):
        return a[0] <= b[0] and a[1] >= b[1] or a[0] >= b[0] and a[1] <= b[1]

    return sum(f(a, b) for a, b in data)


def resu2(data):
    def f(a, b):
        return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1] or b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]

    return sum(f(a, b) for a, b in data)


def test1(resu):
    return resu == 2


def test2(resu):
    return resu == 4


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
