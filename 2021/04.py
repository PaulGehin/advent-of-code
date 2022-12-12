from functools import reduce


def prepare_data(data, test=False):
    new_data = dict()
    new_data["numbers"] = list(map(lambda x: int(x), data[0].split(',')))
    new_data["boards"] = list()
    board = list()
    for line in data[1:]:
        if line == "" and board != []:
            new_data["boards"].append(board)
            board = list()
        elif line != "":
            board.append(list(map(lambda x: int(x), line.split())))
    if board != []:
        new_data["boards"].append(board)
    return new_data


def rows(data):
    new_data = list()
    for i in range(len(data)):
        for y in data[i]:
            temp = list()
            for number in y:
                temp.append({
                    "number": number,
                    "seen": False,
                    "board": i
                })
            new_data.append(temp)
    return new_data


def columns(data):
    new_data = list()
    for k in range(len(data)):
        for j in range(len(data[k][0])):
            temp = list()
            for i in range(len(data[k])):
                temp.append({
                    "number": data[k][i][j],
                    "seen": False,
                    "board": k
                })
            new_data.append(temp)
    return new_data


def every(data):
    return reduce(lambda x, y: x and y["seen"], data, True)


def sum_unmarked(data, board):
    resu = 0
    for x in data:
        for y in x:
            if y["board"] == board and not y["seen"]:
                resu += y["number"]
    return resu // 2


def resu1(data):
    rows_and_columns = rows(data["boards"]) + columns(data["boards"])
    for number in data["numbers"]:
        for row in rows_and_columns:
            for entry in row:
                if entry["number"] == number:
                    entry["seen"] = True
        for row in rows_and_columns:
            if every(row):
                return number * sum_unmarked(rows_and_columns, row[0]["board"])


def resu2(data):
    won = list()
    rows_and_columns = rows(data["boards"]) + columns(data["boards"])
    for number in data["numbers"]:
        for row in rows_and_columns:
            for entry in row:
                if entry["number"] == number:
                    entry["seen"] = True
        for row in rows_and_columns:
            if every(row) and not row[0]["board"] in won:
                won.append(row[0]["board"])
        if len(won) == len(data["boards"]):
            return number * sum_unmarked(rows_and_columns, won[-1])


def test1(resu):
    return resu == 4512


def test2(resu):
    return resu == 1924


if __name__ == "__main__":
    import os
    from utils import run_file

    run_file(abspath=os.path.abspath(__file__), bypasstest=False, submit=True)
