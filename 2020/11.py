def prepare_data(data, test=False):
    y = 0
    resu = dict()
    resu["max_x"] = len(data[0])
    resu["max_y"] = len(data)
    for line in data:
        for x, seat in enumerate(line):
            resu[(x, y)] = seat
        y += 1
    return resu


def number_adjacent(data, seat):
    resu = []
    for i in range(max(0, seat[0] - 1), min(data["max_x"], seat[0] + 2)):
        for j in range(max(0, seat[1] - 1), min(data["max_y"], seat[1] + 2)):
            resu.append(data[(i, j)])
    if data[seat] == "#":
        return resu.count("#") - 1
    else:
        return resu.count("#")


def change_seat(data):
    resu = data.copy()
    for seat in data:
        if not (data[seat] == "." or seat == "max_x" or seat == "max_y"):
            number = number_adjacent(data, seat)
            if number == 0 and data[seat] == "L":
                resu[seat] = "#"
            elif number > 3 and data[seat] == "#":
                resu[seat] = "L"
    return data, resu


def look_adjacent(data, seat):
    resu = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            k = 1
            while 0 <= seat[0] + i * k < data["max_x"] and 0 <= seat[1] + j * k < data["max_y"] and data[
                (seat[0] + i * k, seat[1] + j * k)] == ".":
                k += 1
            if (i, j) != (0, 0) and 0 <= seat[0] + i * k < data["max_x"] and 0 <= seat[1] + j * k < data["max_y"]:
                resu.append(data[(seat[0] + i * k, seat[1] + j * k)])
    return resu.count("#")


def change_seat_look(data):
    resu = data.copy()
    for seat in data:
        if not (data[seat] == "." or seat == "max_x" or seat == "max_y"):
            number = look_adjacent(data, seat)
            if number == 0 and data[seat] == "L":
                resu[seat] = "#"
            elif number > 4 and data[seat] == "#":
                resu[seat] = "L"
    return data, resu


def resu1(data):
    resu = data.copy()
    resu_temp = dict()
    while resu != resu_temp:
        resu_temp, resu = change_seat(resu)
    return [resu[seat] for seat in resu].count("#")


def resu2(data):
    resu = data.copy()
    resu_temp = dict()
    while resu != resu_temp:
        resu_temp, resu = change_seat_look(resu)
    return [resu[seat] for seat in resu].count("#")


def test1(resu):
    return resu == 37


def test2(resu):
    return resu == 26


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
