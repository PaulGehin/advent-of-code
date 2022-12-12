class Sue:
    def __init__(self, number: int):
        self.number = number
        self.values = {}

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __iter__(self):
        return self.values.__iter__()

    def __repr__(self):
        return str(self.__dict__)


def prepare_data(data, test=False):
    def prepare_line(line):
        sep = line.index(":")
        number = int(line[4:sep])
        resu = Sue(number)
        for elem in line[sep + 2:].split(", "):
            key, value = elem.split(": ")
            resu[key] = int(value)
        return resu

    return list(map(prepare_line, data))


ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def valid(sue):
    for key in sue:
        if ticker_tape[key] != sue[key]:
            return sue.number, False
    return sue.number, True


def resu1(data):
    resu = list(map(lambda x: x[0], filter(lambda x: x[1], map(valid, data))))
    return resu[0] if len(resu) == 1 else resu


def valid_2(sue):
    for key in sue:
        if key in ('cats', 'trees') \
                and ticker_tape[key] > sue[key] \
                or key in ('pomeranians', 'goldfish') \
                and ticker_tape[key] < sue[key] \
                or not key in ('cats', 'trees', 'pomeranians', 'goldfish') \
                and ticker_tape[key] != sue[key]:
            return sue.number, False
    return sue.number, True


def resu2(data):
    resu = list(map(lambda x: x[0], filter(
        lambda x: x[1], map(valid_2, data))))
    return resu[0] if len(resu) == 1 else resu


def test1(resu):
    return True


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    import sys

    day = int(os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0])
    year = int(os.path.basename(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    from utils import run

    run(day=day, year=year, bypasstest=True)
