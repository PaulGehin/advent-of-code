def prepare_data(data, test=False):
    resu = {}
    for line in data:
        value, key = line.split(" -> ")
        resu[key] = value
    return resu


def resu1(data):
    resu = {}

    def compute_l_3(key, value):
        if value[1] == "AND":
            resu[key] = compute(value[0]) & compute(value[2])
        elif value[1] == "LSHIFT":
            resu[key] = compute(value[0]) << compute(value[2])
        elif value[1] == "RSHIFT":
            resu[key] = compute(value[0]) >> compute(value[2])
        elif value[1] == "OR":
            resu[key] = compute(value[0]) | compute(value[2])

    def compute(key):
        if not key in data.keys():
            return int(key)
        if not key in resu.keys():
            value = data[key].split(" ")
            length = len(value)
            if length == 1:
                resu[key] = compute(value[0])
            elif length == 2:
                resu[key] = 65535 - compute(value[1])
            elif length == 3:
                compute_l_3(key, value)
        return resu[key]

    return compute("a")


def resu2(data):
    resu = {}

    def compute_l_3(key, value):
        if value[1] == "AND":
            resu[key] = compute(value[0]) & compute(value[2])
        elif value[1] == "LSHIFT":
            resu[key] = compute(value[0]) << compute(value[2])
        elif value[1] == "RSHIFT":
            resu[key] = compute(value[0]) >> compute(value[2])
        elif value[1] == "OR":
            resu[key] = compute(value[0]) | compute(value[2])

    def compute(key):
        if not key in data.keys():
            return int(key)
        if not key in resu.keys():
            value = data[key].split(" ")
            length = len(value)
            if length == 1:
                resu[key] = compute(value[0])
            elif length == 2:
                resu[key] = 65535 - compute(value[1])
            elif length == 3:
                compute_l_3(key, value)
        return resu[key]

    data["b"] = str(compute("a"))
    resu = {}
    return compute("a")


def test1(resu):
    return resu == 65079


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
