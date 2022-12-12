from typing import List


def prepare_data(data, test=False):
    if test:
        split = data.index("---")
        return [[int(i) for i in line.split()] for line in data[:split]],\
               [[int(i) for i in line.split()] for line in data[split + 1:]]
    return [[int(i) for i in line.split()] for line in data]


def resu1(data):
    if len(data) == 2:
        data = data[0]
    return sum([max(row) - min(row) for row in data])


def evenly_divide(row: List[int]) -> int:
    resu = set()
    row.sort()
    for i, a in enumerate(row):
        for b in row[i:]:
            if b % a == 0:
                resu.add(b // a)
    return max(resu)


def resu2(data):
    if len(data) == 2:
        data = data[1]
    return sum([evenly_divide(row) for row in data])


def test1(resu):
    return resu == 18


def test2(resu):
    return resu == 9


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
