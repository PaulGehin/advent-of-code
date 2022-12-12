def prepare_data(data, test=False):
    resu = []
    for line in data:
        new = repr(line).replace('"', '\\"').replace(
            '\'\\"', '"\\"').replace('\\"\'', '\\""')
        resu.append({"raw": line, "interpreted": eval(line), "new": new})
    return resu


def resu1(data):
    def count_diff(line):
        return abs(len(line["raw"]) - len(line["interpreted"]))

    return sum(map(count_diff, data))


def resu2(data):
    def count_diff(line):
        return abs(len(line["new"]) - len(line["raw"]))

    return sum(map(count_diff, data))


def test1(resu):
    return resu == 12


def test2(resu):
    return resu == 19


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
