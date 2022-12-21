def prepare_data(data, test=False):
    resu = {}
    for line in data:
        a, b = line.split(":")
        a = a.strip()
        b = b.strip()
        try:
            b = int(b)
        except ValueError:
            b = b.split()
        resu[a] = b
    return resu, test


def yell(monkey, data, human=None, test=False):
    if human is not None and monkey.startswith("humn"):
        return human
    if isinstance(data[monkey], int):
        return data[monkey]
    a, op, b = data[monkey]
    if human is not None and monkey == "root" and test:
        return int(yell(a, data, human, test)) < int(yell(b, data, human, test))
    if human is not None and monkey == "root":
        return int(yell(a, data, human, test)) > int(yell(b, data, human, test))
    match op:
        case "+":
            return int(yell(a, data, human, test) + yell(b, data, human, test))
        case "-":
            return int(yell(a, data, human, test) - yell(b, data, human, test))
        case "*":
            return int(yell(a, data, human, test) * yell(b, data, human, test))
        case "/":
            return int(yell(a, data, human, test) / yell(b, data, human, test))


def resu1(data):
    return int(yell("root", data[0]))


def resu2(data):
    data, test = data
    low = 0
    high = 1_000_000_000_000_000
    while low < high:
        mid = (low + high) // 2
        if yell("root", data, mid, test):
            low = mid + 1
        else:
            high = mid
    if low not in (0, 1_000_000_000_000_000):
        return low
    print("You must change '>' => '<' in line 24")


def test1(resu):
    return resu == 152


def test2(resu):
    return resu == 301


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
