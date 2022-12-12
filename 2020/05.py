def prepare_data(data, test=False):
    return data


def seat_id(line):
    rows, columns = line[:7], line[7:10]
    mincolumn, maxcolumn, minrow, maxrow = 0, 7, 0, 127
    for character in columns:
        if character == "L":
            maxcolumn = mincolumn + (maxcolumn - mincolumn) // 2
        else:
            mincolumn = mincolumn + (maxcolumn - mincolumn) // 2 + 1
    for character in rows:
        if character == "F":
            maxrow = minrow + (maxrow - minrow) // 2
        else:
            minrow = minrow + (maxrow - minrow) // 2 + 1
    return minrow * 8 + mincolumn


def resu1(data):
    return max(map(seat_id, data))


def resu2(data):
    list_id = list(map(seat_id, data))
    resu = [x for x in range(
        max(list_id)) if x not in list_id and x - 1 in list_id and x + 1 in list_id]
    return resu[0] if len(resu) == 1 else resu


def test1(resu):
    return resu == 820


def test2(resu):
    return True


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
