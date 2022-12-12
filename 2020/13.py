import math


def prepare_data(data, test=False):
    resu = dict()
    resu["start"] = int(data[0])
    resu["bus"] = data[1].split(",")
    return resu


def resu1(data):
    def wait(bus):
        return math.inf, bus if bus == "x" else int(bus) * ((data['start'] // int(bus)) + 1) - data["start"], int(bus)

    resu = min(map(wait, data["bus"]), key=lambda x: x[0])
    return resu[0] * resu[1]


def chinese_remainder(n, a):
    resu = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        resu += a_i * mul_inv(p, n_i) * p
    return resu % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def resu2(data):
    n, a = [], []
    for i, bus in enumerate(data["bus"]):
        if bus != "x":
            n.append(int(bus))
            a.append(int(bus) - i)
    return round(chinese_remainder(n, a))


def test1(resu):
    return resu == 295


def test2(resu):
    return resu == 1068781


if __name__ == "__main__":
    import os
    import sys

    day = int(os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0])
    year = int(os.path.basename(os.path.dirname(os.path.abspath(__file__))))
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))
    from utils import run

    run(day=day, year=year, bypasstest=True)
