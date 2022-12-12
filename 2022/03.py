def prepare_data(data, test=False):
    return data


def resu1(data):
    def f(line):
        for char in line[:len(line) // 2]:
            if char in line[len(line) // 2:]:
                return ord(char) - 96 if ord(char) > 96 else ord(char) - 64 + 26

    return sum(f(x) for x in data)


def resu2(data):
    def f(a, b, c):
        for char in a:
            if char in b and char in c:
                return ord(char) - 96 if ord(char) > 96 else ord(char) - 64 + 26

    return sum(f(x, data[data.index(x) + 1], data[data.index(x) + 2]) for x in data[::3])


def test1(resu):
    return resu == 157


def test2(resu):
    return resu == 70


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
