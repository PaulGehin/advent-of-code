def prepare_data(data, test=False):
    new_data = list()
    for line in data:
        x, y = line.split(" -> ")
        x1, x2 = x.split(',')
        y1, y2 = y.split(',')
        new_data.append({
            "x1": int(x1),
            "x2": int(x2),
            "y1": int(y1),
            "y2": int(y2)
        })
    return new_data


def extract(data, position):
    resu = list()
    for line in data:
        resu.append(line[f"x{position}"])
        resu.append(line[f"y{position}"])
    return resu


def resu1(data):
    ones = extract(data, "1")
    twos = extract(data, "2")
    min_ones = min(ones)
    max_ones = max(ones)
    min_twos = min(twos)
    max_twos = max(twos)

    len_ones = max_ones - min_ones + 1
    len_twos = max_twos - min_twos + 1

    resu = [[0 for _ in range(len_twos)] for _ in range(len_ones)]
    for line in data:
        if line["x1"] == line["y1"]:
            i = line["x1"] - min_ones
            start = min([line["x2"], line["y2"]]) - min_twos
            end = max([line["x2"], line["y2"]]) - min_twos
            for j in range(start, end + 1):
                resu[i][j] += 1
        elif line["x2"] == line["y2"]:
            j = line["x2"] - min_twos
            start = min([line["x1"], line["y1"]]) - min_ones
            end = max([line["x1"], line["y1"]]) - min_ones
            for i in range(start, end + 1):
                resu[i][j] += 1
    return count_resu(resu)


def count_resu(data):
    resu = 0
    for x in data:
        for y in x:
            if y > 1:
                resu += 1
    return resu


def resu2(data):
    ones = extract(data, "1")
    twos = extract(data, "2")
    min_ones = min(ones)
    max_ones = max(ones)
    min_twos = min(twos)
    max_twos = max(twos)

    len_ones = max_ones - min_ones + 1
    len_twos = max_twos - min_twos + 1

    resu = [[0 for _ in range(len_twos)] for _ in range(len_ones)]
    for line in data:
        if line["x1"] == line["y1"]:
            i = line["x1"] - min_ones
            start = min([line["x2"], line["y2"]]) - min_twos
            end = max([line["x2"], line["y2"]]) - min_twos
            for j in range(start, end + 1):
                resu[i][j] += 1
        elif line["x2"] == line["y2"]:
            j = line["x2"] - min_twos
            start = min([line["x1"], line["y1"]]) - min_ones
            end = max([line["x1"], line["y1"]]) - min_ones
            for i in range(start, end + 1):
                resu[i][j] += 1
        else:
            if line["x1"] < line["y1"]:
                offset_one = 1
            else:
                offset_one = -1
            if line["x2"] < line["y2"]:
                offset_two = 1
            else:
                offset_two = -1
            start_one = min([line["x1"], line["y1"]]) - min_ones
            end_one = max([line["x1"], line["y1"]]) - min_ones
            start_two = min([line["x2"], line["y2"]]) - min_twos
            end_two = max([line["x2"], line["y2"]]) - min_twos
            for k in range(end_one - start_one + 1):
                i = line["x1"] - min_ones + offset_one * k
                j = line["x2"] - min_twos + offset_two * k
                resu[i][j] += 1
    return count_resu(resu)


def test1(resu):
    return resu == 5


def test2(resu):
    return resu == 12


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
