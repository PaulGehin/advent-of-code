def prepare_data(data, test=False):
    y = 0
    resu = dict()
    resu["max_x"] = len(data[0])
    resu["max_y"] = len(data)
    for line in data:
        for x, light in enumerate(line):
            resu[(x, y)] = light
        y += 1
    return resu


def number_adjacent(data, light):
    resu = []
    for i in range(max(0, light[0] - 1), min(data["max_x"], light[0] + 2)):
        for j in range(max(0, light[1] - 1), min(data["max_y"], light[1] + 2)):
            resu.append(data[(i, j)])
    if data[light] == "#":
        return resu.count("#") - 1
    else:
        return resu.count("#")


def toggle_light(data):
    resu = data.copy()
    for seat in data:
        if not (seat == "max_x" or seat == "max_y"):
            number = number_adjacent(data, seat)
            if number == 3 and data[seat] == ".":
                resu[seat] = "#"
            elif not number in {2, 3} and data[seat] == "#":
                resu[seat] = "."
    return resu


def toggle_light_2(data):
    resu = data.copy()
    for seat in data:
        if not (seat == "max_x" or seat == "max_y") \
                and not seat in {(0, 0),
                                 (data["max_x"] - 1, 0),
                                 (0, data["max_y"] - 1),
                                 (data["max_x"] - 1, data["max_y"] - 1)}:
            number = number_adjacent(data, seat)
            if number == 3 and data[seat] == ".":
                resu[seat] = "#"
            elif not number in {2, 3} and data[seat] == "#":
                resu[seat] = "."
    return resu


def resu1(data):
    resu = data.copy()
    number = 4 if data["max_x"] == 6 else 100
    for _ in range(number):
        resu = toggle_light(resu)
    return list(resu.values()).count("#")


def resu2(data):
    resu = data.copy()
    for seat in {(0, 0),
                 (data["max_x"] - 1, 0),
                 (0, data["max_y"] - 1),
                 (data["max_x"] - 1, data["max_y"] - 1)}:
        resu[seat] = "#"
    number = 5 if data["max_x"] == 6 else 100
    for _ in range(number):
        resu = toggle_light_2(resu)
    return list(resu.values()).count("#")


def test1(resu):
    return resu == 4


def test2(resu):
    return resu == 17


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
